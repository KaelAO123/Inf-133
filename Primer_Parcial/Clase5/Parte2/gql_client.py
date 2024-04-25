import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
response = requests.post(url, json={'query': query_lista})
print(response.text,"\n\n")




query_id = """
    {
        estudiantePorId(id: 2){
            nombre
            apellido
        }
    }
"""

response = requests.post(url, json={'query': query_id})
print(response.text,"\n\n")


query_nom_apel = """
    {
        estudiantePorNombreApellido(nombre: "Jose",apellido:"Lopez"){
            id
            nombre
            apellido
            carrera
        }
    }
"""

response = requests.post(url, json={'query': query_nom_apel})
print(response.text,"\n\n")


query_carrera = """
    {
        estudiantePorCarrera(carrera: "Arquitectura"){
            id
            nombre
            apellido
            carrera
        }
    }
"""

response = requests.post(url, json={'query': query_carrera})
print(response.text,"\n\n")





query_crear1 = """
    mutation{
            crearEstudiante(nombre:"Angel", apellido:"Gomez",carrera:"Arquitectura"){
                estudiante{
                    id
                    nombre
                    apellido
                    carrera
            }
        }
    }
"""
query_crear2 = """
    mutation{
            crearEstudiante(nombre:"Rafael", apellido:"Sanginez",carrera:"Arquitectura"){
                estudiante{
                    id
                    nombre
                    apellido
                    carrera
            }
        }
    }
"""
query_crear3 = """
    mutation{
            crearEstudiante(nombre:"Edgar", apellido:"Vallivian",carrera:"Arquitectura"){
                estudiante{
                    id
                    nombre
                    apellido
                    carrera
            }
        }
    }
"""

requests.post(url, json={'query': query_crear1})
requests.post(url, json={'query': query_crear2})
response = requests.post(url, json={'query': query_crear3})

print(response.text,"\n\n")

response = requests.post(url, json={'query': query_lista})
print(response.text,"\n\n")

response = requests.post(url, json={'query': query_carrera})
print(response.text,"\n\n")

query_actualizar = """
    mutation{
            actualizarEstudiante(nombre:"Jose", apellido:"Lopez",carrera:"Topologia",id:2){
                estudiante{
                    id
                    nombre
                    apellido
                    carrera
            }
        }
    }
"""
response = requests.post(url, json={'query': query_actualizar})
print(response.text,"\n\n")


query_eliminar_carreras = """
    mutation{
            deleteEstudianteCarrera(carrera:"Arquitectura"){
                estudiante{
                    id
                    nombre
                    apellido
                    carrera
            }
        }
    }
"""
response = requests.post(url, json={'query': query_eliminar_carreras})
print(response.text,"\n\n")

response = requests.post(url, json={'query': query_lista})
print(response.text,"\n\n")