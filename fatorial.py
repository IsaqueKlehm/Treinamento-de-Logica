numero = int(input('Digite o numero para ver seu fatorial: '))
apoio = 1

for i in range(1, numero+1):
    apoio *= i

print(apoio)