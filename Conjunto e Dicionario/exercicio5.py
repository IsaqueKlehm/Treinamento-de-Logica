# Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
# Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. 
# Sua tarefa é criar um programa que realize essa operação.

equipe_a = set(input("Digite a tarefa da equipe A: ").lower().split(", "))
equipe_b = set(input("Digite a tarefa da equipe B: ").lower().split(", "))
tarefa_unida = equipe_a.union(equipe_b)
print(", ".join(tarefa_unida))
remove = input("Digite a tarefa que deseja remover: ").lower()
tarefa_unida.remove(remove)
print(", ".join(tarefa_unida))