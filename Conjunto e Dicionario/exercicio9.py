participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

participante_removido = input("Digite o nome do participante que deseja remove-lo: ").title()

for workshop, nomes in participantes.items():
    nomes.discard(participante_removido)
print("Lista atualizada de participantes: ")
for workshop, nomes in participantes.items():
    print(f'{workshop} {nomes}')