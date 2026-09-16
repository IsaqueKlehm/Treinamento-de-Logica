texto1 = set(input("Digite a frase: ").lower().split(" "))
texto2 = set(input("Digite outra frase: ").lower().split(" "))

iguais = texto1.intersection(texto2)

print(", ".join(iguais))