# Ruta Cero
Python scripts created to offer a routing SMS service

The project has 3 python files:
<dl>
  <dt>run.py:</dt> 
  <dd>initial script, starts a server listening on port 5000 for POST petitions, it recieves as params a string with the format <i>[origin,dest]</i>, if you send the right parameters then it returns de route, if no it returns an error</dd>
  <dt>mapsConnector.py:</dt>
  <dd>File with a class called Maps that requires a GoogleMapsAPI key, you can create your own key <a href="https://developers.google.com/maps/web-services/">right here</a>  .This connector generates GET requests and parses JSON responses into nice msgs</dd>
  <dt>mongoConnector.py:</dt>
  <dd>File with a class called MongoConnector that connects to a local running MongoDB on default Mongo port that uses the information from de MapatonDB in GeoJson format.
  <a href="https://github.com/LabPLC/MapatonAPI">Go to MapatonAPI repo</a></dd>
</dl>
