import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")
print(response.text)
print("##########################################\n")

response = requests.get(f"{url}/posts/2")
print(response.text)
print("##########################################\n")


nueva_publicacion = {
    "title":"Mi experiencia como dev",
    "content":"yyy... no sé, esta historia es realmente triste si lo tengo que decir"
}
response = requests.post(f"{url}/posts",json=nueva_publicacion)
print(response.text)
print("##########################################\n")
response = requests.get(f"{url}/posts")
print(response.text)
print("##########################################\n")


response = requests.put(f"{url}/posts/3", json={"title":"en progreso", "content":"nada"})
print(response.text)
print("##########################################\n")

response = requests.delete(f"{url}/posts/3")
print(response.text)
print("##########################################\n")