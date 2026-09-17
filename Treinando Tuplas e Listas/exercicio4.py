# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e 
# gera um relatório com todos os produtos juntos?

estoque_um = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque_dois = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_combinado = estoque_um + estoque_dois

print(f"""
Produtos do estoque 1 (separados por vírgula): {estoque_um}\n
Produtos do estoque 2 (separados por vírgula): {estoque_dois}\n
Estoque combinado:\n{estoque_combinado}
        """)