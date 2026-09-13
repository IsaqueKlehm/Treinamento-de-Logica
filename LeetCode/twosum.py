numeros = [2, 7, 11, 15]
numero_alvo = 30

for i in range(len(numeros)):
    for j in range(i, len(numeros)):
        soma = numeros[i] + numeros[j]
        print(soma)
        if soma == numero_alvo:
            print(f'[{i}, {j}]')
