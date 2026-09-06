aluno = input('Digite o nome do aluno: ')
notas = []

for i in range(1, 4):
    nota = int(input(f'Digite o valor da nota {i}: ')) 
    notas.append(nota)

soma_das_notas = sum(notas)
quantidade_de_notas = len(notas)

media = soma_das_notas/quantidade_de_notas

if media >= 7:
    print(f'O aluno {aluno} foi aprovado com uma média de {media}')
elif media >= 5 and media < 7:
    print(f'O aluno {aluno} foi Recuperação com uma média de {media}')
else:
    print(f'O aluno {aluno} foi Reprovado com uma média de {media}')
