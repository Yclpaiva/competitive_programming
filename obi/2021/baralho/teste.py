input = input()

copas = []
ouros = []
espadas = []
paus = []

def carta_existe(carta,naipe):
    for i in range(len(naipe)):
        if carta == naipe[i]:
            if naipe == copas:
                block_naipe['C'] = True
            if naipe == ouros:
                block_naipe['U'] = True
            if naipe == espadas:
                block_naipe['E'] = True
            if naipe == paus:
                block_naipe['P'] = True
    return False

block_naipe = {
    'C': False,
    'U': False,
    'E': False,
    'P': False
}

for i in range(0,len(input), 3):
    carta = int(input[i])*10 + int(input[i+1])
    naipe = input[i+2] 
    if naipe == 'C':
        carta_existe(carta,copas)
        if not block_naipe["C"]: 
            copas.append(carta)
    if naipe == 'U':
        carta_existe(carta,ouros)
        if not block_naipe["U"]: 
            ouros.append(carta)
    if naipe == 'E':
        carta_existe(carta,espadas)
        if not block_naipe["E"]: 
            espadas.append(carta)
    if naipe == 'P':
        carta_existe(carta,paus)
        if not block_naipe["P"]: 
            paus.append(carta)

if block_naipe['C']:
    print('erro')
else:
    print(13- len(copas))

if block_naipe['E']:
    print('erro')
else:
    print(13 -len(espadas))

if block_naipe['U']:
    print('erro')
else:
    print(13- len(ouros))

if block_naipe['P']:
    print('erro')
else:
    print(13 - len(paus))


