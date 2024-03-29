import requests

url = "http://localhost:8000/pizzas"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_taco = {
    "base": "Grande",
    "salsa": "Delgada",
    "toppings": ["Jamon", "Queso"],
    "guiso": "sin guiso"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
edit_taco = {
    "base": "Grande",
    "salsa": "Mediana",
    "toppings": ["Jamon", "Queso", "JAJA"],
    "guiso": "Nada de guiso"
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())