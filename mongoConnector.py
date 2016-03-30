# Copyright (c) 2016 Ruben Cuadra
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#  http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software  distributed under the License # is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pymongo
from mapsConnector import Maps

class MongoConnector():
	def __init__(self,database,host='localhost',port=27017):
		self.cnxn=pymongo.MongoClient(host,port)
		self.db=self.cnxn[database]

from geopy.distance import vincenty
def TransportMe(origenAsText,destinoAsText):      #Debe regresar rutas a tomar, paradas iniciales y finales
	a,t=Maps(),MongoConnector('-MongoDbName-').db['-MongoDbObjectName-']
	cl,dl = a.textToLatLng(origenAsText),a.textToLatLng(destinoAsText)
	nls,ndls=[],[]
	query={'st_asgeojson':{'$near':{'$geometry':{'type':'Point','coordinates':[0,0],'$maxDistance':50}}}}
	print 'Origen: %s    Destino: %s'%(cl,dl)
	rutasATomar=[]
	'''SET NEAR ORIGIN VALUES'''
	lat,lng = cl.split(',')
	query['st_asgeojson']['$near']['$geometry']['coordinates'][0]= float(lng)
	query['st_asgeojson']['$near']['$geometry']['coordinates'][1]= float(lat)
	nls = [s for s in t.find(query)]
	'''SET NEAR DESTINATION VALUES'''
	lat,lng = dl.split(',')
	query['st_asgeojson']['$near']['$geometry']['coordinates'][0]= float(lng)
	query['st_asgeojson']['$near']['$geometry']['coordinates'][1]= float(lat)
	ndls    = [s for s in t.find(query)]
	ruta={}

	for s in nls: 
		if s in ndls:  
			nrst=[10000,''] 
			ruta['codigo']=s['route_short_name']
			ruta['nombre']=s['route_long_name']
			roo=s['st_asgeojson']['coordinates'][0]
			for i in xrange(0,len(roo)):
				co='%s,%s'%(roo[i][1],roo[i][0])
				calc=vincenty(cl,co).km
				if calc<nrst[0]:
					nrst=calc,co
			ruta['subir']=nrst[1]  
			nrst=[10000,''] 		  
			for i in xrange(0,len(roo)):
				co='%s,%s'%(roo[i][1],roo[i][0])
				calc=vincenty(dl,co).km
				if calc<nrst[0]:
					nrst=calc,co
			ruta['bajar']=nrst[1]
			return ruta
	return



