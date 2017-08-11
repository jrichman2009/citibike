import json
import requests

bike_data = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')

bike_data = json.loads(bike_data.text)



station_info = int((bike_data['data']['stations'][0].get('station_id')))
    
print(type(station_info))

for item in bike_data['data']['stations']:
    station_number = int(item.get('station_id'))
    station_info = item.get
    if station_number != 410:
        continue
    else:
        bikes = item.get('num_bikes_available')
        if int(item.get('num_bikes_available')) < 40:
            print('there are only {} bikes avail!'.format(bikes))
               
##        print(station_number)
##        station_info = item
##        print(item)

