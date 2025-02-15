import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo libro
url = f"{BASE_URL}/libros"
nuevo_libro =         {
            "titulo": "Harry Potter",
            "autor": "J. K. Rolling",
            "edicion": "Infinita",
            "disponibilidad":5,
        }
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Crear el segundo libro
nuevo_libro_2 =         {
            "titulo": "Como Ganar Cocodrilos",
            "autor": "Erick Picavia",
            "edicion": "Finita",
            "disponibilidad":7,
        }
nuevo_libro_3 =         {
            "titulo": "Como Enclochar",
            "autor": "Erick Picavia",
            "edicion": "Finita",
            "disponibilidad":7,
        }
response = requests.post(url, json=nuevo_libro_2, headers=headers)
print("\nCreando el segundo libro:")
print(response.json())

# Obtener la lista de todos los animales
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de animales:")
print(response.json())

# Obtener un libro específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.get(url, headers=headers)
print("\nDetalles del libro con ID 1:")
print(response.json())

# Actualizar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
datos_actualizacion =         {
            "titulo": "Como Ganar Tigres",
            "autor": "Erick Picavia",
            "edicion": "Infinita",
            "disponibilidad":5,
        }
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el libro con ID 1:")
print(response.json())

# Eliminar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el libro con ID 1:")
if response.status_code == 204:
    print(f"Animal con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
