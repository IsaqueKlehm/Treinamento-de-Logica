numero = input("Digite a sua senha: ").split()
lista = []
for i in numero:
    # Verifica se é negativo
    if i == "-":
        print(i, end="")
        lista.append(i)
    try:
        if int(i):
            pass
    except:
        if i == "-":
            pass
        else:
            break
    try:
        # Se tem numero nas letra
        if int(i):
            print(i, end="")
            lista.append(i)
    except:
        pass
if len(lista) == 0:
    print(0)