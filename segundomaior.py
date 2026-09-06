maior = 0
segundo_maior = 0

for i in range(1, 6):
    numero = int(input("Digite seu numero"))
    while numero < 0:
        print('\nNUMERO NEGATIVOS NÃO SÃO PERMITIDOS\nDIGITE NOVAMENTE OUTRO NUMERO\n')
        numero = int(input("Digite seu numero"))

    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior:
        segundo_maior = numero

print(maior)
print(segundo_maior)

