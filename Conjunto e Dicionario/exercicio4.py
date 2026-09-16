# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões 
# faz parte das permissões principais de um sistema. 
# Sua tarefa é desenvolver um programa que receba duas listas de permissões 
# e verifique se a segunda lista está contida na primeira.

permissoes_principais = set(input("Digite as permissões principais: ").lower().split(", "))
permissoes_solicitadas = set(input("Digite as permissões que deseja solicitar: ").lower().split(", "))

if permissoes_solicitadas.issubset(permissoes_principais):
    print("As permissões fazem parte das permissões principais.")
else:
    print("As permissões solicitadas NÃO fazem parte das permissões principais")

