def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



qnt_numeros = int(input())
resultados = []
num_recebe = []
for i in range(qnt_numeros):
    num_recebe.append(int(input()))

for recebe in num_recebe:
    for j in range(recebe):
        for k in range(recebe):
            if (j+k == recebe) and (j < k) and not eh_primo(j) and not eh_primo(k):
                resultados.append([recebe,j,k])

apareceu = False
for i in range(qnt_numeros):
    calc_soma = 1_000_000_000
    for j in range(len(resultados)):
        if num_recebe[i] == resultados[j][0]:
            calc_soma = min(calc_soma ,resultados[j][2]-resultados[j][1])
            apareceu = True

    if not apareceu:
        print(-1)
    for j in range(len(resultados)):
        if num_recebe[i] == resultados[j][0]:
            if resultados[j][2]-resultados[j][1] == calc_soma:
                print(resultados[j][1],resultados[j][2])
    
