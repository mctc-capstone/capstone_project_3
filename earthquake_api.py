import requests
from main import getCoordinates
from datetime import datetime

cityState = 'Parkfield, CA'  # example location until we figure out how to incorporate main.py user coordinates with this API
location_coordinates = getCoordinates(cityState)

latitude = location_coordinates[0]
longitude = location_coordinates[1]

earthquake_url = (f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson'
                  f'&starttime=2021-01-01'
                  f'&endtime=now'
                  f'&latitude={latitude}'
                  f'&longitude={longitude}'
                  f'&maxradiuskm=24'
                  f'&minmagnitude=3.0')

earthquake_data = requests.get(earthquake_url).json()
list_of_earthquakes = earthquake_data['features']

for earthquake in list_of_earthquakes:
    wanted_data = earthquake['properties']
    location = wanted_data['place']
    time = wanted_data['time']
    date = datetime.fromtimestamp(time / 1000).date()
    magnitude = wanted_data['mag']

    print(f'Location: {location} *** Date: {date} *** Magnitude: {magnitude}')



