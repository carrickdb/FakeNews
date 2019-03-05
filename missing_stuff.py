import pickle, pprint


with open("points.pkl", 'rb') as f:
    points = pickle.load(f)

pp = pprint.PrettyPrinter(indent=4)
point_county = {}
for point in points:
    pp.pprint(point)
    assert False
    try:
        county_info = point['geographies']['Counties'][0]
        if 'BASENAME' in county_info:
            county = point['geographies']['Counties'][0]['BASENAME']
            point = point['full_name']
            state = point['geographies']['States'][0]['STUSAB']
            point_county[point] = (county, state)
    except:
        pp.pprint(point)
        assert False

with open("point_county.pkl", 'wb') as f:
    pickle.dump(point_county, f)


# with open("neighborhoods.pkl", 'rb') as f:
#     neighs = pickle.load(f)
#
# pp = pprint.PrettyPrinter(indent=4)
# neigh_county = {}
# for neigh in neighs:
#     try:
#         county_info = neigh['geographies']['Counties'][0]
#         if 'BASENAME' in county_info:
#             county = neigh['geographies']['Counties'][0]['BASENAME']
#             neighborhood = neigh['full_name']
#             state = neigh['geographies']['States'][0]['STUSAB']
#             neigh_county[neighborhood] = (county, state)
#     except:
#         pp.pprint(neigh)
#         assert False
#
# with open("neigh_county.pkl", 'wb') as f:
#     pickle.dump(neigh_county, f)



# # Missing cities:
# with open("missing_cities_county.pkl", 'rb') as f:
#     missing_cities = pickle.load(f)
#
# new_cities = {}
# pp = pprint.PrettyPrinter(indent=4)
# # classes = set()
# # classes.add('waterway')
# i = 0
# for k, v in missing_cities.items():
#     # print(k)
#     # pp.pprint(v)
#     # if v['class'] not in classes:
#     #     print(v['class'])
#     i += 1
#     city, state = k.split(',')
#     print(state)
#     print(v['geographies']['Counties'][0]['BASENAME'])
#     print(city)
#     if i > 3:
#         assert False
#     print()


"""
Pine Creek, MI
{   'boundingbox': ['42.0985407', '42.1116679', '-85.261711', '-85.2517337'],
    'class': 'waterway',
    'display_name': 'Pine Creek, Calhoun County, Michigan, 49011, USA',
    'geographies': {   '2010 Census Blocks': [   {   'AREALAND': 0,
                                                     'AREAWATER': 14937,
                                                     'BASENAME': '1034',
                                                     'BLKGRP': '1',
                                                     'BLOCK': '1034',
                                                     'CENTLAT': '+42.1061368',
                                                     'CENTLON': '-085.2570977',
                                                     'COUNTY': '025',
                                                     'FUNCSTAT': 'S',
                                                     'GEOID': '260250028001034',
                                                     'INTPTLAT': '+42.1068808',
                                                     'INTPTLON': '-085.2575298',
                                                     'LSADC': 'BK',
                                                     'LWBLKTYP': 'W',
                                                     'MTFCC': 'G5040',
                                                     'NAME': 'Block 1034',
                                                     'OBJECTID': 1874024,
                                                     'OID': 210403969719027,
                                                     'STATE': '26',
                                                     'STGEOMETRY.AREA': 27155.457,
                                                     'STGEOMETRY.LEN': 1727.374,
                                                     'SUFFIX': '',
                                                     'TRACT': '002800'}],
                       'Census Tracts': [   {   'AREALAND': 185485338,
                                                'AREAWATER': 1600523,
                                                'BASENAME': '28',
                                                'CENTLAT': '+42.1159219',
                                                'CENTLON': '-085.1773391',
                                                'COUNTY': '025',
                                                'FUNCSTAT': 'S',
                                                'GEOID': '26025002800',
                                                'INTPTLAT': '+42.1119650',
                                                'INTPTLON': '-085.1905693',
                                                'LSADC': 'CT',
                                                'MTFCC': 'G5020',
                                                'NAME': 'Census Tract 28',
                                                'OBJECTID': 24594,
                                                'OID': 20790495651871,
                                                'STATE': '26',
                                                'STGEOMETRY.AREA': 340234016.0,
                                                'STGEOMETRY.LEN': 78211.945,
                                                'TRACT': '002800'}],
                       'Counties': [   {   'AREALAND': 1829206358,
                                           'AREAWATER': 31260656,
                                           'BASENAME': 'Calhoun',
                                           'CENTLAT': '+42.2465045',
                                           'CENTLON': '-085.0055767',
                                           'COUNTY': '025',
                                           'COUNTYCC': 'H1',
                                           'COUNTYNS': '01622955',
                                           'FUNCSTAT': 'A',
                                           'GEOID': '26025',
                                           'INTPTLAT': '+42.2429896',
                                           'INTPTLON': '-085.0123853',
                                           'LSADC': '06',
                                           'MTFCC': 'G4020',
                                           'NAME': 'Calhoun County',
                                           'OBJECTID': 1804,
                                           'OID': 27590495637677,
                                           'STATE': '26',
                                           'STGEOMETRY.AREA': 3397364740.0,
                                           'STGEOMETRY.LEN': 234935.81}],
                       'States': [   {   'AREALAND': 146600419992,
                                         'AREAWATER': 103886386840,
                                         'BASENAME': 'Michigan',
                                         'CENTLAT': '+44.8382252',
                                         'CENTLON': '-085.6650496',
                                         'DIVISION': '3',
                                         'FUNCSTAT': 'A',
                                         'GEOID': '26',
                                         'INTPTLAT': '+44.8441768',
                                         'INTPTLON': '-085.6604907',
                                         'LSADC': '00',
                                         'MTFCC': 'G4000',
                                         'NAME': 'Michigan',
                                         'OBJECTID': 43,
                                         'OID': 2749048217992,
                                         'REGION': '2',
                                         'STATE': '26',
                                         'STATENS': '01779789',
                                         'STGEOMETRY.AREA': 499744571000.0,
                                         'STGEOMETRY.LEN': 3795814.0,
                                         'STUSAB': 'MI'}]},
    'importance': 0.625,
    'input': {   'benchmark': {   'benchmarkDescription': 'Public Address '
                                                          'Ranges - Current '
                                                          'Benchmark',
                                  'benchmarkName': 'Public_AR_Current',
                                  'id': '4',
                                  'isDefault': False},
                 'location': {'x': -85.2574545, 'y': 42.1055547},
                 'vintage': {   'id': '4',
                                'isDefault': True,
                                'vintageDescription': 'Current Vintage - '
                                                      'Current Benchmark',
                                'vintageName': 'Current_Current'}},
    'lat': '42.1055547',
    'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. '
               'https://osm.org/copyright',
    'lon': '-85.2574545',
    'osm_id': '367488925',
    'osm_type': 'way',
    'place_id': '159615798',
    'type': 'river'}
"""
