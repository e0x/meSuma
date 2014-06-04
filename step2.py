import requests
import sys


def get_data(arg):
	"""
	this function wait a RNC how argument and use it 
	to generate the url for the data request.
	"""
        prefix = 'http://data.developers.do/api/v1/empresas/'
	sufix  = '.json'
	url = prefix + arg + sufix
	r = requests.get(url).json()
	try:
		print 'Nombre:', r['nombre']
	except:
	        print 'No encontro datos'


if __name__ == '__main__':
	arg = sys.argv[1]
        get_data(arg)
