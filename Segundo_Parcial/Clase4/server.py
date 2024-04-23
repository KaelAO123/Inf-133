# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.

app = Flask(__name__)

# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET",])
def sumar():
    numero1 = (request.args.get("num1"))
    numero2 = (request.args.get("num2"))
    if not numero1:
        return (
            jsonify({"Error":"Se necesita el primer numero"},400)
        )
    if not numero2:
        return (
            jsonify({"Error":"Se necesita el segundo numero"},400)
        )
    numero1=int(numero1)
    numero2=int(numero2)
    return jsonify({"mensaje":f"La suma es: {numero1+numero2}"})

@app.route("/palindromo", methods=["GET",])
def palindromo():
    cadena = (request.args.get("cadena"))
    if not cadena:
        return (
            jsonify({"Error":"Se necesita una cadena"},400)
        )
    cadena_invertida = cadena[::-1]
    if cadena_invertida == cadena:
        return jsonify({"mensaje":f"La cadena {cadena} es palindroma"})
    else:
        return jsonify({"mensaje":f"La cadena {cadena} no es palindroma"})

@app.route("/contar", methods=["GET",])
def contar():
    cadena = (request.args.get("cadena"))
    vocal = request.args.get("vocal")
    if not cadena:
        return (
            jsonify({"Error":"Se necesita una cadena"},400)
        )
    if not vocal:
        return (
            jsonify({"Error":"Se necesita una vocal"},400)
        )
    cantidad_vocal = cadena.count(vocal)
    return jsonify({"mensaje":f"Cadena {cadena} tiene {cantidad_vocal} {vocal}"})

# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()