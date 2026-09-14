convidados = set()

while True:
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ").title()

    if nome == "Sair":
        break

    convidados.add(nome)

print(f"Convidados confirmaos: {', '.join(convidados)}")
