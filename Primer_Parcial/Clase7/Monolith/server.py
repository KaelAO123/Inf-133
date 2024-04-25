from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

# Base de datos simulada de publicaciones
db = {
    1: {
        "title": "Mi primera publicación",
        "content": "¡Hola mundo! Esta es mi primera publicación en el blog.",
    },
    2: {
        "title": "Otra publicación",
        "content": "¡Bienvenidos a mi blog! Aquí hay otra publicación.",
    },
}
class PublicacionesServicio:
    @staticmethod
    def crear_publicacion(data):
        title = data.get("title")
        content = data.get("content")
        new_post_id = max(db.keys()) + 1
        db[new_post_id] = {"title": title, "content": content}
        return new_post_id
        
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar las cabeceras de respuesta

        # Generar la respuesta JSON de acuerdo a la solicitud
        if self.path == "/posts":
            HTTPDataHandler.handle_response(self,200,db.values())
        elif self.path.startswith("/posts/"):
            post_id = int(self.path.split("/")[-1])
            post = db.get(post_id)
            if post:
                HTTPDataHandler.handle_response(self,200,post)
            else:
                HTTPDataHandler.handle_response(self,404,{"Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self,404,{"Ruta no valida"})

    def do_POST(self):
        data = HTTPDataHandler.handle_reader(self)
        if self.path == "/posts":
            new_post_id=PublicacionesServicio.crear_publicacion(data)
            HTTPDataHandler.handle_response(self,201,new_post_id)
        else:
            HTTPDataHandler.handle_response(self,404,{"Ruta no valida"})

    def do_PUT(self):
        # Actualizar una publicación existente
        if self.path.startswith("/posts/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                data = HTTPDataHandler.handle_reader(self)
                db[post_id]["title"] = data.get("title")[0]
                db[post_id]["content"] = data.get("content")
                HTTPDataHandler.handle_response(self,200,post_id)
            else:
                HTTPDataHandler.handle_response(self,404,{"Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self,404,{"Ruta no valida"})

    def do_DELETE(self):
        # Eliminar una publicación existente
        if self.path.startswith("/posts/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                del db[post_id]
                HTTPDataHandler.handle_response(self,204,{""})
            else:
                HTTPDataHandler.handle_response(self,404,{"Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self,404,{"Ruta no valida"})


def run_server(server_class=HTTPServer, handler_class=BlogHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()