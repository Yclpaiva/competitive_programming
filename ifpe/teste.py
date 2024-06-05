recebe = input()
qnt_lojas, qnt_tabaco_inicial = recebe.split()
qnt_lojas = int(qnt_lojas)
qnt_tabaco_inicial = int(qnt_tabaco_inicial)

dist = list(map(int, input().split()))
tbc = list(map(int, input().split()))

vezes_que_parou = 0
k = qnt_tabaco_inicial
posicao_saci = -1 

while True:
    if dist[qnt_lojas -1] <= k:
        print(vezes_que_parou,"\n")
        break
    max_anda_index = 0
    variavel = posicao_saci
    for variavel in range(qnt_lojas):
        if posicao_saci == -1:

            if dist[variavel] > k:
                max_anda_index = variavel
                vezes_que_parou += 1
                break
        else:
            if (dist[variavel]- dist[posicao_saci]) > k:
                max_anda_index = variavel
                vezes_que_parou += 1
                break
    index = 0 
    maior_distancia_pecorrivel = 0
    for i in range(max_anda_index):
        if (dist[i] + tbc[i]) > maior_distancia_pecorrivel:
            index = i
    maior_distancia_pecorrivel = dist[index] + tbc[index]
    posicao_saci = index 
    k = tbc[index]
    if k < (dist[index+1] - dist[index]):
        print(-1,"\n")
        break

    
    if k >= dist[qnt_lojas-1] - dist[posicao_saci]:
        print(vezes_que_parou,"\n")
        break




