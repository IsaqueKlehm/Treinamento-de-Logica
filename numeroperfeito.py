numero = int(input("Digite um número: "))
numeros = []

i = 1

while i < numero:
    if numero % i == 0:
        str(numeros.append(i))
        i += 1
    else:
        i += 1

soma = " + ".join(map(str, numeros))
print(soma)

print(f'{soma} = {numero}')
