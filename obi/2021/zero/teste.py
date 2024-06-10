quantidade_numeros = int(input())


numeros = []
for i in range(quantidade_numeros):
    numero = int(input())
    if numero == 0:
        numeros.pop()
    else:
        numeros.append(numero)

print(sum(numeros))
