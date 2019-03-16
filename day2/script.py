from urllib import request
import json
import math

API_KEY = 'd98c933280f7b5e572b6d902565d9d8bb0f76bba'
CONTRACT_ID = 'Marseille'

def run(latitude, longitude):
	url = f"https://api.jcdecaux.com/vls/v1/stations?apiKey={API_KEY}&contract={CONTRACT_ID}"
	contents = json.loads(request.urlopen(url).read())

	min_d = 100000
	min_d_name = ''
	min_available = 0

	for station in contents:
		x1 = station['position']['lat']
		y1 = station['position']['lng']

		d = math.sqrt((x1 - latitude) ** 2 + (y1 - longitude) ** 2)

		if d < min_d:
			min_d = d
			min_d_name = station['name']
			min_available = station['available_bikes']

	# Trouver la station la plus proche d'ici ?
	print(min_d_name, min_available)

if __name__ == '__main__':
	latitude = 43.302
	longitude = 5.377
	run(latitude, longitude)