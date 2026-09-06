numero = int(input("Digite um número: "))

for numero_atual in range(2, numero + 1):
    primo = True

    for i in range(2, numero_atual):
        if numero_atual % i == 0:
            primo = False
            break

    if primo:
        print(numero_atual)