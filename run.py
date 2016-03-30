#!/usr/bin/env python
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

from flask import Flask, request, redirect
import twilio.twiml
import mapsConnector
from mongoConnector import TransportMe
app = Flask(__name__)
@app.route("/", methods=['POST'])
def hello_monkey():
	from_number = request.values.get('From', None)
	print "Mensaje recibido desde:" + from_number
	resp=None
	body = request.values.get('Body', None)
	print "Msg Body: " + body
	resp = twilio.twiml.Response()
	if ',' in body:
		locationFromSMS,locationToSMS = body.split(',')
		if locationToSMS and locationFromSMS:
			infoAboutRoute=TransportMe(locationFromSMS, locationToSMS)  
			fromLocation = maps.textToLatLng(locationFromSMS)
			toFirstStop=infoAboutRoute['bajar']
			fromLastStop=infoAboutRoute['subir'] 
			toLastLocation = maps.textToLatLng(locationToSMS)
			routeName=infoAboutRoute['nombre']+'||'+infoAboutRoute['codigo']
			firstStop=maps.getReferenceOnLocation(infoAboutRoute['subir'])
			lasStop=maps.getReferenceOnLocation(infoAboutRoute['bajar'])
			directionsFromInitUntilFirstStop=maps.getDirections(fromLocation,toFirstStop)
			directionsFromLastStopUntilDest =maps.getDirections(fromLastStop,toLastLocation)
			resp.message('%s %s %s %s'%(maps.getRouteLine(directionsFromInitUntilFirstStop[0]),maps.getRouteLine(directionsFromInitUntilFirstStop[-1], route=routeName,stop=firstStop),maps.getRouteLine('stop',stop=lasStop),maps.getRouteLine(directionsFromLastStopUntilDest[-1])))
			del msg
	else:
		resp.message("No entiendo lo que quieres decir, recuerda el formato es: [origen],[destino]")
	return str(resp)
if __name__ == "__main__":
	maps=mapsConnector.Maps('KeyForGoogleAPI')
	app.debug = True
	app.run(host='0.0.0.0')