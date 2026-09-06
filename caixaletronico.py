saque = float(input("Digite a quantidade de dinheiro que deseja sacar: "))

notas = [100, 50, 20, 10, 5, 2]

for nota in notas:

    quantidade = saque // nota
    sobra = saque % nota
    print(f'Quantidade de Notas: {quantidade} de {nota}\nSobra: {sobra}')
    saque = sobra



    