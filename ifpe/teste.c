#include <stdio.h>
#include <stdlib.h>

int main() {
    int qnt_lojas, qnt_tabaco_inicial;
    scanf("%d %d", &qnt_lojas, &qnt_tabaco_inicial);

    int dist[qnt_lojas];
    int tbc[qnt_lojas];
    
    for (int i = 0; i < qnt_lojas; i++) {
        scanf("%d", &dist[i]);
    }

    for (int i = 0; i < qnt_lojas; i++) {
        scanf("%d", &tbc[i]);
    }

    int vezes_que_parou = 0;
    int k = qnt_tabaco_inicial;
    int posicao_saci = -1;

    while (1) {
        if (dist[qnt_lojas - 1] <= k) {
            printf("%d\n", vezes_que_parou);
            break;
        }

        int max_anda_index = 0;
        for (int variavel = 0; variavel < qnt_lojas; variavel++) {
            if (posicao_saci == -1) {
                if (dist[variavel] > k) {
                    max_anda_index = variavel;
                    vezes_que_parou++;
                    break;
                }
            } else {
                if ((dist[variavel] - dist[posicao_saci]) > k) {
                    max_anda_index = variavel;
                    vezes_que_parou++;
                    break;
                }
            }
        }

        int index = 0;
        int maior_distancia_pecorrivel = 0;
        for (int i = 0; i < max_anda_index; i++) {
            if ((dist[i] + tbc[i]) > maior_distancia_pecorrivel) {
                index = i;
                maior_distancia_pecorrivel = dist[i] + tbc[i];
            }
        }

        posicao_saci = index;
        k = tbc[index];

        if (k < (dist[index + 1] - dist[index])) {
            printf("-1\n");
            break;
        }

        if (k >= dist[qnt_lojas - 1] - dist[posicao_saci]) {
            printf("%d\n", vezes_que_parou);
            break;
        }
    }

    return 0;
}

