"""
Joins counties and vote percentages with geo data.

"""

import json
import csv, pickle
import pprint

user_type = "con"


with open("geotags_" + user_type + "_recent.json", 'r') as f:
    geo_data = json.load(f)

votes = {}
with open("processed_votes.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        county = row[0].lower()  # CALos Angeles <- format
        points = float(row[2]) - float(row[1])
        votes[county] = points

counties = {}
with open("cities.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        state = row[0].lower()
        county = row[1].lower()
        city = row[2].strip().lower()
        if county[-5:] == " city":
            county = county[:-5]
        if state not in counties:
            counties[state] = {}
        counties[state][city] = county
with open("more_cities.csv", 'r') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        if len(row) > 4:
            state = row[1].lower()
            county = row[3].lower()
            city = row[4].lower()
            if len(county) > 5 and county[-5] == "city":
                county = county[:-5]
            if state not in counties:
                counties[state] = {}
            counties[state][city] = county
with open("neigh_county.pkl", 'rb') as f:
    counties.update(pickle.load(f))
with open("point_county.pkl", 'rb') as f:
    counties.update(pickle.load(f))

states = {}
with open("state_votes", 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        states[row[0]] = float(row[1]) - float(row[2])

i = 0
revised_geo = {}
single_countries = {}
missing_cities = set()
missing_points = set()
missing_admin = set()
missing_neighborhoods = set()
missing_county_votes = set()
missing_states = set()
for userid, places in geo_data.items():
    revised_date_geo = []
    visited_countries = set()
    for date_geo in places:
        place = date_geo['place']
        if place != None:
            place_type = place['place_type']
            country = place['country_code']
            if country != '':
                visited_countries.add(country)
            if country == 'US':
                if place_type == 'city':
                    city = place['name'].lower()
                    state = place['full_name'][-2:].lower()
                    if state not in counties:
                        missing_states.add(state)
                    else:
                        cities = counties[state]
                        if city not in cities:
                            missing_cities.add(place['full_name'])
                        else:
                            if state == "ak":
                                county = "alaska"
                            else:
                                county = cities[city].lower()
                                if county[-5:] == " city":
                                    county = county[:-5]
                            state_county = state + county
                            date_geo['county'] = state_county
                            if state_county in votes:
                                points = votes[state_county]
                                date_geo['points'] = points
                            elif state != 'ak':
                                missing_county_votes.add(state_county)
                elif place_type == 'poi' or place_type == 'neighborhood':
                    neigh_name = place['full_name']
                    if neigh_name in counties:
                        county, state = counties[neigh_name]
                        state_county = state+county
                        if state_county in votes:
                            points = votes[state_county]
                            date_geo['points'] = points
                        elif state != 'ak':
                            missing_county_votes.add(state_county)
                    elif place_type == 'neighborhood':
                        missing_neighborhoods.add(json.dumps(place))
                    elif place_type == 'poi':
                        missing_points.add(json.dumps(place))
                else:
                    full_name = place['full_name'].split(',')[0]
                    if full_name in states:
                        date_geo['points'] = states['full_name']
                    else:
                        missing_admin.add(place)
            revised_date_geo.append(date_geo)
    if len(visited_countries) == 1:
        single_country = list(visited_countries)[0]
        if single_country in single_countries:
            single_countries[single_country] += 1
        else:
            single_countries[single_country] = 1
    revised_geo[userid] = revised_date_geo

print("Missing cities:", len(missing_cities))
with open("missing_cities.txt", 'w') as f:
    for city in missing_cities:
        f.write(city + '\n')

with open("points.json", 'w') as f:
    for point in missing_points:
        f.write(point)
        f.write('\n')

with open("neighborhoods.json", 'w') as f:
    for neigh in missing_neighborhoods:
        f.write(neigh)
        f.write('\n')

with open("missing_admin.json", 'w') as f:
    for area in missing_admin:
        f.write(area)
        f.write('\n')

print()
print("Missing counties in vote tallies:")
for county in missing_county_votes:
    print(county)

print()
print("Missing states:")
for state in missing_states:
    print(state)

# print()
# countries = sorted(list(single_countries.items()), key=lambda x: x[1], reverse=True)
# with open("country_tally_" + user_type + ".csv", 'w') as f:
#     writer = csv.writer(f)
#     for country, count in countries:
#         writer.writerow([country, count])

with open("with_votes_" + user_type + ".json", 'w') as f:
    json.dump(revised_geo, f)


"""
city:
{'attributes': {},
 'bounding_box': {'coordinates': [[[-122.514926, 37.708075],
                                   [-122.357031, 37.708075],
                                   [-122.357031, 37.833238],
                                   [-122.514926, 37.833238]]],
                  'type': 'Polygon'},
 'contained_within': [],
 'country': 'United States',
 'country_code': 'US',
 'full_name': 'San Francisco, CA',
 'id': '5a110d312052166f',
 'name': 'San Francisco',
 'place_type': 'city',
 'url': 'https://api.twitter.com/1.1/geo/id/5a110d312052166f.json'}

admin:
 {   'attributes': {},
    'bounding_box': {   'coordinates': [   [   [-124.482003, 32.528832],
                                               [-114.131212, 32.528832],
                                               [-114.131212, 42.009519],
                                               [-124.482003, 42.009519]]],
                        'type': 'Polygon'},
    'contained_within': [],
    'country': 'United States',
    'country_code': 'US',
    'full_name': 'California, USA',
    'id': 'fbd6d2f5a4e4a15e',
    'name': 'California',
    'place_type': 'admin',
    'url': 'https://api.twitter.com/1.1/geo/id/fbd6d2f5a4e4a15e.json'}

neighborhood:
{"id": "3496512730330cc3", "url": "https://api.twitter.com/1.1/geo/id/3496512730330cc3.json",
"place_type": "neighborhood", "name": "Downtown Jacksonville", "full_name": "Downtown Jacksonville, FL",
"country_code": "US", "country": "United States", "contained_within": [], "
bounding_box": {"type": "Polygon", "coordinates": [[[-81.6673775, 30.3206946], [-81.6461, 30.3206946],
[-81.6461, 30.33406], [-81.6673775, 30.33406]]]}, "attributes": {}}

"""
