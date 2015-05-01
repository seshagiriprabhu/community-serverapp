#/usr/bin/env python2
"""
A file to load some dummy data into the db
"""
import json
import requests
import os

headers = {'Content-type': 'application/json',\
        'Accept': 'application/json'}

BASE_URL = 'http://localhost:8000/'
register_url = BASE_URL + 'register/'
geofence_url = BASE_URL + 'geofence/'
userlocation_url = BASE_URL + 'location/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
register_file = os.path.join(BASE_DIR, 'registeration.json')
geofence_file = os.path.join(BASE_DIR, 'geofence.json')
userlocation_file = os.path.join(BASE_DIR, 'userlocation.json')

files = [register_file, geofence_file, userlocation_file]
urls = [register_url, geofence_url, userlocation_url]

# Load the JSON data from files and post it in server
for x in xrange(len(files)):
    with open(files[x]) as data_file:
        json_data = json.load(data_file)
        for data in json_data:
            processed_data = json.dumps(data)
            r = requests.post(urls[x], data=processed_data,\
                    headers=headers)
            print r.text
r.close()
