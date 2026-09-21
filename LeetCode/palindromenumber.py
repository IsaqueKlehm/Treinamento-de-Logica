def palindromo(numero):
    numero_str = str(numero) 
    if numero_str == numero_str[::-1]:
        return True
    else:
        return False

