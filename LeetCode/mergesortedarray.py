lista1 = [1, 2, 3, 0, 0, 0]
lista2 = [2, 4, 5]

i = 2
j = 2
k = 5

while j >= 0:
    if i >= 0 and lista1[i] > lista2[j]:
        lista1[k] = lista1[i]
        i -= 1
    else:
        lista1[k] = lista2[j]
        j -= 1

    k -= 1

print(lista1)

    




