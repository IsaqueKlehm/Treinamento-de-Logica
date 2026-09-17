# Roberto está organizando sua despensa e quer verificar se determinados itens 
# já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens 
# disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

Lista = ['pão', 'leite', 'ovo']

item = input('Digite o item qeu você quer verificar: ')
if item in Lista:
    print(f'Contém {item} na lista ja')
else:
    print(f'Não contém {item} na lista')
