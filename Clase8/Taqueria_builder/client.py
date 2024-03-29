import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

response = requests.get(url)
print(response.json())


mi_taco = {
    "base": "Grande",
    "salsa": "Mayonesa",
    "toppings": ["Jamon", "Queso", "Aceitunas moradas"],
    "guiso": "sin guiso"
}

response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())

edit_taco = {
    "base": "Grande",
    "salsa": "Ketchup",
    "toppings": ["Jamon", "Queso", "Aceiutanas verdes"],
    "guiso": "Nada de guiso"
}
response = requests.put(url+"/1", json=edit_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())


response = requests.delete(url + "/1")
print(response.json())

response = requests.get(url)
print(response.json())