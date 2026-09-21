lista = [4, 1, 2, 1, 2]
def numeros(n):
    for i in n:
        quantidade = n.count(i)
        if quantidade <= 1:
            return i

numeros(lista)


