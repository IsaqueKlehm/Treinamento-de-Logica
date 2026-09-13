frase = "A man, a plan, a canal: Panama".lower()

def palindromo (frase):
    limpa = ""

    for caracter in frase:
        if caracter.isalnum():
            limpa += caracter

    if limpa == limpa[::-1]:
        print(True)
    else:
        print(False)

palindromo(frase)