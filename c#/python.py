palavra = input()
palavra2 = input()

palavra = palavra.split().sort()
palavra2 = palavra2.split().sort()

if palavra == palavra2:
    print('S')
else:
    print('N')
