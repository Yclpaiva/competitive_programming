palavra = input()
palavra2 = input()

palavra = sorted(list(palavra))
palavra2 = sorted(list(palavra2))

print(palavra,palavra2)
while "*" in palavra2:
    palavra2.remove("*")

if len(palavra2) < len(palavra):
    counter = 0
    for letra in palavra2:
        if letra in palavra:
            counter += 1
    if counter == len(palavra2):
        print('S')
else:
    if palavra == palavra2:
        print('S')
    else:
        print('N')
