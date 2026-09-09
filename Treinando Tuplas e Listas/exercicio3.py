voluntarios = []

escolha = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
voluntarios.append(escolha)

while escolha != 'sair':
    escolha = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
    if escolha == 'sair':
        print(f'Voluntários Registrados: {voluntarios}')
        break
    else:
        voluntarios.append(escolha)