# address_to_coordinates.py

import geocoder
import numpy
import pdb
import pandas



def query_coordinates(address):
  g = geocoder.google(address)
  coordinates = g.latlng
  return(coordinates)


# import data
address_csv_location = '~/dev/one-off-analysis/Python/address_to_coordinates/test addresses.csv'

#with open(address_csv_location, 'rb')

address_data = numpy.recfromcsv(address_csv_location, delimiter = ',')

df = pandas.read_csv(address_csv_location, sep = ',')

df['query_address'] = df[''] + ' ' + df[]

# query

pdb.set_trace()

