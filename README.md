# Reverse_geo_coding
Written in Python to get postal address based on latitude and longitude using open street map API

This project is to address below real life problem. Please note that data given is just sample. Real data cannot be shared. Real data is also large in volume.

Problem Statement: An organization needs to know postal address corresponsing to latitude and longitude, so that appropriate customer segmentation can be done. It'll also help to understand the density of customer for a particular time - which in turn help proper campaign.

Data file: Sample data file contains latitude and longitude. 

Solution: I have applied open API from open street map. The program is written in python.

Prerequisite:

You need to have Python installed version 3.5 or above and environment setup properly
You need to have GeoPy installed

Usage: It is written and tested for Windows 7 OS. It should run in other environment also, but not tested. May be little bit changes are required as per demand of that OS. Please keep data file in same folder where source program is located. Data file is without any header. From command line following command should be executed.

python getAddress.py

Output: It will generate a comma separated file, "latlongadd.csv" in same folder where datafile and source program are located. Output file will have three fields separated with comma. Fields are as below

latitude
longitude
Postal address having comma within value


************ Enjoy and don't forget to give credit if it helps ****************
