#!/usr/bin/python
################################################################
#   Author: Jnanendra Sarkar
#
################################################################
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

ifile = 'latlong.csv'
ofile = 'latlongadd.csv'

fin = open(ifile, 'rt')
fot = open(ofile, 'wt')

def do_geocode(latlong):
    try:
        return geoCode.reverse(latlong)
    except GeocoderTimedOut:
        return do_geocode(latlong)

		
geoCode = Nominatim(timeout=1)

for line in fin:
	line = line.lstrip()
	line = line.rstrip()
	templine = line.split(",")
	lat = templine[0]
	lon = templine[1]
	location = geoCode.reverse(line)
	fullLine = lat + ',' + lon + ',' + location.address
	fot.writelines(fullLine)
	fot.writelines("\n")
fin.close()
fot.close()
