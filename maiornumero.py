numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

print(f'O {maior} é o maior numero entre {numero1} e {numero2}')