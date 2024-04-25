from zeep import Client

client = Client('http://localhost:8000')

# NumberToDollars
print("NumberToDollars")
result = client.service.NumberToDollars(numero=33)
print(result)

# Suma de dos numeros
print("\nSuma de dos numeros")
result2 = client.service.SumaDosNumeros(3,4)
print(result2)

# Es palindromo
print("\nEs palindromo?")
result3 = client.service.EsPalindromo("Ana")
print(result3)