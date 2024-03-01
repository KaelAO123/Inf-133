import requests
url="http://localhost:8000/"

# Buscar nombres que empiecen por P
ruta_nombre=url+"buscar_nombre/P"
nombre_P = requests.request(method="GET",url=ruta_nombre)
print(f"Todos los nombres con P: {nombre_P.text}")

# Contar carreras
ruta_nombre=url+"contar_carreras"
nroCarrera = requests.request(method="GET",url=ruta_nombre)
print(f"Nro de carreras que hay: {nroCarrera.text}")

# Contar carreras
ruta_nombre=url+"contar_estudiantes"
nroEstudiantes = requests.request(method="GET",url=ruta_nombre)
print(f"Nro de los estudiante que hay: {nroEstudiantes.text}")