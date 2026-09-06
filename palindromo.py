palavra = input("Digite a palavra para ver se é Palíndromo: ")

if palavra == palavra[::-1]:
    print("É Palíndromo")
else:
    print("Não é Palíndromo")