import requests
url  =  "http://localhost:8000/"
ruta_get = url+"lista_estudiantes"
get_response = requests.request(method = "GET",url = ruta_get)
print(get_response.text)
print("##################################\n\n")
ruta_post = url+"agrega_estudiante"
nuevo_estudiante = {
    "nombre":"PEdrodaosdsamo",
    "apellido":"Perez",
    "carrera": "Ingenieria Agronomica"
}
post_response  =  requests.request(method = "POST",url = ruta_post,json = nuevo_estudiante)
print(post_response.text)

# Buscar nombres que empiecen por P
ruta_nombre = url+"buscar_nombre/P"
nombre_P  =  requests.request(method = "GET",url = ruta_nombre)
print(nombre_P.text)

# Contar carreras
ruta_nombre = url+"contar_carreras"
nroCarrera  =  requests.request(method = "GET",url = ruta_nombre)
print(nroCarrera.text)

# Contar carreras
ruta_nombre = url+"contar_estudiantes"
nroEstudiantes  =  requests.request(method = "GET",url = ruta_nombre)
print(nroEstudiantes.text)