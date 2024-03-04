import requests

url = "http://localhost:8000/"

ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(f"{get_response.text} \n")

ruta_get = url + "estudiantes?apellido=Anaya"
get_response = requests.request(method="GET", url=ruta_get)
print(f"{get_response.text} \n")

ruta_get = url + "estudiantes?carrera=Informatica"
get_response = requests.request(method="GET", url=ruta_get)
print(f"{get_response.text} \n")

ruta_get = url+"estudiantes?nombre=Pedrito&carrera=Informatica&apellido=Reyes"
get_response = requests.request(method="GET", url=ruta_get)
print(f"{get_response.text} \n")