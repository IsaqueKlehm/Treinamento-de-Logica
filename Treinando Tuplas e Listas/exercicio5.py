lista = ['Ana', 'Pedro', 'Carlos']

nome = str(input('Digite o nome do novo convidado: '))
posicao = int(input('Digite a posição na qual deseja inserir o convidado:  '))

lista.insert(posicao-1, nome)

print(lista)