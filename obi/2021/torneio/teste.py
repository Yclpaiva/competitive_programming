vitorias = 0
for i in range(6):
    valor_input = input()
    if valor_input == 'V':
        vitorias += 1

if vitorias == 5 or vitorias == 6:
    print(1)
if vitorias == 3 or vitorias == 4:
    print(2)
if vitorias == 1 or vitorias == 2:
    print(3)
if vitorias == 0:
    print(-1)
