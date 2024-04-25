import requests

# Definir la consulta GraphQL
query = """
    {
        hello
    }
"""
query2 = """ 
    {
        goobye
    }
"""
query3 = """ 
    {
        hello
        goobye
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

response = requests.post(url, json={'query': query2})
print(response.text)

response = requests.post(url, json={'query': query3})
print(response.text)