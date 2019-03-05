import csv

"""
Converts file with votes by county and party to a pivot table with each county only listed once

"""


counties = []
with open("county_votes.csv", 'r') as f:
    with open("processed_votes.csv", 'a') as g:
        reader = csv.reader(f)
        writer = csv.writer(g)
        header = next(reader)
        curr_county = None
        GOP = 0
        DEM = 0
        third = 0
        for row in reader:
            state_county = row[1] + row[2]
            party = row[3]
            num_votes = int(float(row[4]))
            if state_county != curr_county:
                if curr_county:
                    total = GOP + DEM + third
                    writer.writerow([state_county, GOP/total, DEM/total, third/total])
                curr_county = state_county
                GOP = 0
                DEM = 0
                third = 0
            if party == "GOP":
                GOP = num_votes
            elif party == "DEM":
                DEM = num_votes
            else:
                third = num_votes
