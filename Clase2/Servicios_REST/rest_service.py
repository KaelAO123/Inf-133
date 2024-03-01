from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Felipe",
        "apellido": "Reyes",
        "carrera": "Neutriologo",
    },
    {
        "id": 3,
        "nombre": "Eduardo",
        "apellido": "Barja",
        "carrera": "Albanieria",
    },
    {
        "id": 4,
        "nombre": "Pedrito",
        "apellido": "Carvallo",
        "carrera": "Ingeniería de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/buscar_nombre/"):
            letra = (self.path.split("/")[-1]).lower()
            estudianteNom = filter(lambda estudiante: estudiante["nombre"][0].lower() == letra,estudiantes)
            if (estudianteNom):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(list(estudianteNom)).encode("utf-8"))
        elif self.path.startswith("/contar_carreras"):
            letra = (self.path.split("/")[-1]).lower()
            nroCarreras = []
            for carrera in estudiantes:
                if carrera["carrera"] not in nroCarreras:
                    nroCarreras.append(carrera["carrera"])
            if (nroCarreras):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(len(nroCarreras)).encode("utf-8"))
        elif self.path.startswith("/contar_estudiantes"):
            if (estudiantes):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(len(estudiantes)).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()