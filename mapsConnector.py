# -*- coding: utf-8 -*- 
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

from googlemaps import Client
import requests , json
class Maps():
	def __init__(self,key):
		self.key=key
		self.con = Client(key=self.key)
	def getDirections(self,origin,destination,mode='walking'):
		r,a=self.con.directions(origin,destination,mode=mode)[0]['legs'][0]['steps'],[]
		for i in r:
			a.append(i['html_instructions'])
		return a
	def textToLatLng(self,text):
		r=self.con.geocode(text,language='ES-MX')[0]['geometry']['location']
		return '%s,%s'%(r['lat'],r['lng'])
	def getReferenceOnLocation(self,latLngAsString):
		lat,lng=latLngAsString.split(',')
		nearbyS='$MAPS_API?key=%s&location=%s&rankby=distance'%(self.key,latLngAsString)
		return json.loads(requests.get(nearbyS).text)['results'][0]['name']

	def getKeyWords(self,string,start='<b>',end='</b>'): 
		words=[]
		for i in (lambda x:(i for i in xrange(0,x.count(start))))(string):
			string=string[string.find(start)+3:]
			words.append(string[:string.find(end)])
		return words
	def getRouteLine(self,line,route=None, stop=None):
		k = self.getKeyWords(line)
		if route and stop: 
			return 'Continua hasta %s y abordas la ruta %s en la %s '%(k[0], route, stop)
		elif stop: 
			return 'Desciende en la %s'%stop
		else:		
			if len(k)>2:
				return 'Voltea hacia el %s, camina desde %s hacia %s '%(k[0],k[1],k[2])
			else:
				return 'Dirigete hacia %s '%k[0]