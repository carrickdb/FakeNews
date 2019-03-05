import json, csv
from datetime import datetime

type = 'lib'

with open("FINAL_" + type + ".json", 'r') as f:
    data = json.load(f)

vectors = []

for id, geotags in data.items():
    vector = [1]
    # put geotags in ascending order by date
    date_points = []
    for tag in geotags:
        if 'points' in tag:
            datestr = tag['date']
            date = datetime.strptime(datestr, "%a %b %d %H:%M:%S %z %Y")
            points = tag['points']
            date_points.append((date, points))
    date_points = sorted(date_points, key=lambda x: x[0])
    # if len(date_points) > 10:
    #     for date, points in date_points:
    #         print(date, points)
    #     assert False
    if len(date_points) > 1:
        erraticism = 0
        prev_points = date_points[0][1]
        for date, points in date_points[1:]:
            if points != prev_points:
                erraticism += abs(points - prev_points)
            prev_points = points
        erraticism /= len(date_points) - 1
        # print(erraticism)
        vector.append(erraticism)
        vectors.append(vector)


with open("vectors_erraticism_" + type + ".csv", 'w') as f:
    writer = csv.writer(f)
    for vector in vectors:
        writer.writerow(vector)
