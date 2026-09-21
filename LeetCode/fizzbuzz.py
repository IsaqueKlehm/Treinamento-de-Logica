def fizzbuzz(n):
    lista = []
    for i in range(1, n+1):
        if i % 15 == 0:
            lista.append("FizzBuzz")
            continue
        elif i % 3 == 0:
            lista.append("Fizz")
            continue
        elif i % 5 == 0:
            lista.append("Buzz")
            continue
        lista.append(str(i))
    return lista
print(fizzbuzz(100))



