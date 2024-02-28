import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
card_number="BT1-010"
url= f"https://digimoncard.io/api-public/search.php?card={card_number}"
response = requests.request(
    method="GET",
    url=url,
    headers={"Content-Type":"application/json"},
    data={}
)
print(response.text)
estudiantes=[{
    "id":1,
    "nombre":"Pedrito",
    "apellido":"Garcia",
    "carrera":"Ingenieria de Sistemas",
}]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existe"}).encode("utf-8"))
