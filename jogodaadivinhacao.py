import random as rd

numero_aleatorio = rd.randint(1, 100)
print(numero_aleatorio)
numero_escolhido = int(input("Digite um numero de 1 a 100: "))
tentativa = 1


while numero_aleatorio != numero_escolhido:

    if numero_escolhido <  numero_aleatorio:
        print("O numero é maior")

    elif numero_escolhido > numero_aleatorio:
        print("O numero é menor")

    numero_escolhido = int(input("Digite um numero de 1 a 100: "))
    tentativa += 1

print(f"PARABÉNS!\nO número era {numero_aleatorio}\nVocê acertou com {tentativa} tentativas")
