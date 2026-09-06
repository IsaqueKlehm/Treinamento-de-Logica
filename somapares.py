numero = int(input('Digite o numero: '))
par = 0

for i in range(1, numero+1):
    if i % 2 == 0:
        par += i
    else:
        continue
print(par)