import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'nombre': 'Kae'}
response = requests.get(url+'saludar', params=params)

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)


# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'num1': '32', 'num2':'32'}
response = requests.get(url+'sumar?num1=5&num2=3')

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'cadena': 'reconocer'}
response = requests.get(url+'palindromo?cadena=”reconocer”')

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'cadena': 'exepciones','vocal':'e'}
response = requests.get(url+'contar?cadena=exepciones&vocal=e')

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)