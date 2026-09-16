# Ana percebeu que, após o cadastro inicial dos produtos, 
# precisa atualizar a quantidade de um item específico no estoque. 
# Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, 
# atualizando essa informação no dicionário de estoque.

estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

print(estoque)

produto_escolha = input("Digite o nome do produto que deseja mudar a quantidade no estoque: ")
quantidade_escolha = int(input("Digite a quantidade que deseja adicionar: "))

if produto_escolha in estoque:
    estoque[produto_escolha] = quantidade_escolha
    print(estoque)
else:
    print("Nn foi achado")
