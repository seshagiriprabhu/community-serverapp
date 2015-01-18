#/usr/bin/env python2
"""
A file to load some dummy data into the db
"""
import json
import requests
import os

BASE_URL = 'http://localhost:8000/'
register_url = BASE_URL + 'register/'
geofence_url = BASE_URL + 'geofence/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
register_file = os.path.join(BASE_DIR, 'registeration.json')
geofence_file = os.path.join(BASE_DIR, 'geofence.json')

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

# Load the JSON data from registeration.json file and post it in server
with open(register_file) as data_file:
    register_json_data = json.load(data_file)
    for data in register_json_data:
        register_data = json.dumps(data)
        r = requests.post(register_url, data=register_data, headers=headers)
        print r.text

# Load the JSON data from geofence.json file and post it in server
with open(geofence_file) as data_file:
    geofence_json_data = json.load(data_file)
    for data in geofence_json_data:
        geofence_data = json.dumps(data)
        r = requests.post(geofence_url, data=geofence_data, headers=headers)
        print r.text

r.close()
