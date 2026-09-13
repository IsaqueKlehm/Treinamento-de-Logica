numeros = [1, 2, 3, 1]

for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] == numeros[j]:
            print(True)
    
