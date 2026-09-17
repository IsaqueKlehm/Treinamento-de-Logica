# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
# Elas querem um programa que mostre:

# Quais itens apareceram nas duas listas

# Quais foram exclusivos de Laura

# Quais foram exclusivos da Ana

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

lista1 = set(input("Digite a lista de compra da pessoa 1: ").lower().split(", "))
lista2 = set(input("Digite a lista de compra da pessoa 2: ").lower().split(", "))

repetidos = lista1.intersection(lista2)
diferente_lista1 = lista1.difference(lista2)
diferente_lista2 = lista2.difference(lista1)

print(f'\nEm ambas as lista contem: {", ".join(repetidos)}')
print(f'Na lista da pessoa 1 contém: {", ".join(diferente_lista1)}')
print(f'Na lista da pessoa 2 contém: {", ".join(diferente_lista2)}\n')
