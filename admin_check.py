import json, pprint

user_type = "con"

with open("with_votes_" + user_type + ".json", 'r') as f:
    geo_data = json.load(f)

for id, tags in geo_data.items():
    for tag in tags:
        place = tag['place']
        if place:
            pp = pprint.PrettyPrinter(indent=4)
            place_type = place['place_type']
            if place_type == 'admin' and place['country_code'] == 'US':
                pp.pprint(place)
                assert False
