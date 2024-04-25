from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from zeep import Client

def NumberToDollars(numero):
    client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
    )
    result = client.service.NumberToWords(numero)
    return "Tu numero es: {}!".format(result)

def SumaDosNumeros(a,b):
    suma = a+b
    return suma

def EsPalindromo(palabra):
    palabra=palabra.lower()
    aux=palabra[::-1]
    sw=palabra==aux
    return sw

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000",
    action="http://localhost:8000",
    namespace="http://localhost:8000",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "NumberToDollars",
    NumberToDollars,
    returns={"result":str},
    args={"numero":int},
)
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"suma":int},
    args={
        "a":int,
        "b":int,
        },
)
dispatcher.register_function(
    "EsPalindromo",
    EsPalindromo,
    returns={"sw":bool},
    args={"palabra":str},
)

server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher = dispatcher
print("servidor SOAP iniciando en http://localhost:8000")
server.serve_forever()