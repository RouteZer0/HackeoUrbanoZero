# Ruta Cero
Python scripts created to offer a routing SMS service

The project has 3 python files:
	1.- run.py :
		initial script, starts a server listening on port 5000 for POST petitions, it recieves as params a string with the format [origin,dest]
	2.- mapsConnector.py : 
		File with a class called Maps that requires a GoogleMapsAPI, you can create your own [`https://developers.google.com/maps/web-services/`](here)* .This connector do GET requests and parses JSON responses into nice msgs
	3.- mongoConnector.py :
		File with a class called MongoConnector that connects to a local running MongoDB that uses the information from de MapatonDB in GeoJson format. [`https://github.com/LabPLC/MapatonAPI`](Go to MapatonAPI repo)* 
	