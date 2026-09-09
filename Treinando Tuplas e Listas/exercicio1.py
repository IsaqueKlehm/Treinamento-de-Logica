Lista = ['pão', 'leite', 'ovo']

item = input('Digite o item qeu você quer verificar: ')
if item in Lista:
    print(f'Contém {item} na lista ja')
else:
    print(f'Não contém {item} na lista')
