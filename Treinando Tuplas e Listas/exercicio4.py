estoque_um = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque_dois = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_combinado = estoque_um + estoque_dois

print(f"""
Produtos do estoque 1 (separados por vírgula): {estoque_um}\n
Produtos do estoque 2 (separados por vírgula): {estoque_dois}\n
Estoque combinado:\n{estoque_combinado}
        """)