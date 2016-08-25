#!/usr/bin/env python
import csv
import sys
import json
from geopy.geocoders import Nominatim
import requests
import xmltodict

geolocator = Nominatim()
geocoded = {}

with open(sys.argv[1], 'r') as csvfile:
  headers = csv.reader(csvfile).next()
  for k in headers:
    if k != 'Date':
      s = k.replace('Cyclists', '').replace('Total', '').replace('total', '').replace('Cycle Counter', '').replace('_', ' ').replace('Counter', '').strip() + ' cycleway, Auckland, New Zealand'
      if k == 'Curran St total':
        wid = 24145920
      elif k == 'East_Coast_Road Cyclists':
        wid = 301620750
      elif k == 'Grafton Bridge Cyclists':
        wid = 291093994
      elif k == 'Grafton Road Cyclists':
        wid = 118778208
      elif k == 'Great South Road Total':
        wid = 282838687
      elif k == 'HighBrook Cyclists':
        wid = 87232682
      elif k == 'Hopetoun Street Cyclists':
        wid = 37094421
      elif k == 'Lagoon_Drive Cyclists':
        wid = 379038288
      elif k == 'Lake Road Total':
        wid = 147780657
      elif k == 'Mangere Bridge Cyclists':
        wid = 347000114
      elif k == 'Nelson Street Cyclists':
        wid = 384462271
      elif k == 'Nelson Street Lightpath Counter Cyclists':
        wid = 350201288
      elif k == 'NW Cycleway Kingsland Cyclists':
        wid = 24501729
      elif k == 'NW Cycleway TeAtatu Cyclists':
        wid = 23215865
      elif k == 'Orewa Path Cyclists':
        wid = 188036601
      elif k == 'Quay St (Vector Arena) total':
        wid = 294457658
      elif k == 'Quay Street Totem Cyclists':
        wid = 429972757
      elif k == 'SH20 Dominion Road Cyclists':
        wid = 64201924
      elif k == 'Symonds St Total':
        wid = 302551360
      elif k == 'TeWero Bridge Bike Counter Cyclists':
        wid = 429009401
      elif k == 'Twin Streams Cyclists':
        wid = 55565399
      elif k == 'Upper Harbour New Cyclists':
        wid = 38898630
      elif k == 'Victoris St West total':
        wid = 149490337
      else:
        location = geolocator.geocode(s, exactly_one=True)
        wid = location.raw['osm_id']
      xml = requests.get('https://www.openstreetmap.org/api/0.6/way/{}/full'.format(wid)).text
      d = xmltodict.parse(xml)
      geocoded[k] = d

print(json.dumps(geocoded, indent=2))