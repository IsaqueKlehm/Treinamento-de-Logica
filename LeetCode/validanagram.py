anagram = "anagram"
nagaram = "nagaram"

if len(anagram) == len(nagaram):
    for letra in anagram:
        if anagram.count(letra) != nagaram.count(letra):
            print(False)
            break
    else:
        print(True)
            


