numero = int(input("Digite o número pra ver a tabuada dele: "))

for i in range(1, numero+1):
    total = numero * i
    print(f'{numero} * {i} = {total}')