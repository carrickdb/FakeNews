import pandas as pd
import numpy as np
from bs4 import BeautifulSoup # for scraping 2016 results
import urllib.request as urllib2
from collections import Counter
import json


# each page has a summary table that rolls up results at the state level
# get rid of it
def cond(x):
    if x:
        return x.startswith("table ec-table") and not "table ec-table ec-table-summary" in x
    else:
        return False


# list of state abbreviations
states = ['AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

# headers for csv export
data = [['state_abbr', 'county_name', 'party', 'votes_total_2016']]

# loop through each state's web page http://townhall.com/election/2016/president/%s/county, where %s is the state abbr
# add in Request Agent in request header
header = {'User-Agent': 'Mozilla/5.0'}
for state in states:
    site = 'https://townhall.com/election/2016/president/' + state + '/county'
    request = urllib2.Request(site,headers=header)
    page = urllib2.urlopen(request).read()
    soup = BeautifulSoup(page, "html.parser")

    # loop through each <table> tag with .ec-table class
    tables = soup.findAll('table', attrs={'class':cond})

    for table in tables:
        if table.findParent("table") is None:
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                # first tbody tr has four td
                if len(cols) == 4:
                    # strip text from each td
                    divs = cols[0].find_all('div')
                    county = divs[0].text.strip()
                    party = cols[1]['class'][0]
                    total_votes_2016 = int(cols[2].text.strip().replace(',','').replace('-','0'))
                # all other tbody tr have three td
                else:
                    party = cols[1]['class'][0]
                    total_votes_2016 = int(cols[1].text.strip().replace(',','').replace('-','0'))

                #combine each row's results
                rowData = [state,county,party,total_votes_2016]
                data.append(rowData)


townhall = pd.DataFrame(data) # throw results in dataframe
new_header = townhall.iloc[0] #grab the first row for the header
townhall = townhall[1:] #take the data less the header row
townhall.columns = new_header #set the header row as the df header
townhall['votes_total_2016'] = townhall['votes_total_2016'].astype('float64')
print(townhall.shape[0])

townhall.to_csv("county_votes.csv")
