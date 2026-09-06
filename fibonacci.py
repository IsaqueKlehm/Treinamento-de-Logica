numero = int(input("Digite o numero para ver a sequencia de fibonacci: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(numero)
print(resultado)