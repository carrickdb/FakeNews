import json
from datetime import datetime, timedelta


MAX_INTL = 44/365
type = 'control'

revised_geotags = {}

with open("geotags_control_recent.json", 'r') as f:
	for line in f:
		id_geotags = json.loads(line.strip())

		for id, geotags in id_geotags.items():
			date_country = []
			actual_geotags = []
			for tag in geotags:
				datestr = tag['date']
				date = datetime.strptime(datestr, "%a %b %d %H:%M:%S %z %Y")
				if tag['place']:
					country = tag['place']['country']
					date_country.append((date, country))
					actual_geotags.append(tag)
			if not date_country:
				continue
			date_country = sorted(date_country, key=lambda x: x[0])
			total_time = date_country[-1][0] - date_country[0][0]
			prev_country = date_country[0][1]
			prev_time = date_country[0][0]
			intl_time = timedelta()
			countries = set()
			for i in range(len(date_country)):
				curr_country = date_country[i][1]
				if not prev_country:
					prev_country = curr_country
					continue
				curr_time = date_country[i][0]
				countries.add(curr_country)
				if curr_country and curr_country != prev_country:
					if prev_country != 'United States':
						intl_time += curr_time - prev_time
					prev_country = curr_country
				prev_time = curr_time
			add = False
			if 'United States' in countries:
				if total_time > timedelta():
					intl_travel = intl_time/total_time
					if intl_travel < MAX_INTL:
						add = True
				else:
					add = True
			if add:
				revised_geotags[id] = actual_geotags


with open("travel_" + type + ".json", 'w') as f:
    json.dump(revised_geotags, f)



# date: Fri Nov 30 16:44:49 +0000 2018
