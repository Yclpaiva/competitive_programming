#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Função para verificar se um número é primo
bool eh_primo(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    long int qnt_numeros;
    scanf("%d", &qnt_numeros);

    long long int num_recebe[qnt_numeros];
    for (int i = 0; i < qnt_numeros; i++) {
        scanf("%lld", &num_recebe[i]);
    }

    int resultados[1000][3]; // Armazena os resultados (número, j, k)
    int resultado_count = 0;

    for (int i = 0; i < qnt_numeros; i++) {
        int recebe = num_recebe[i];
        for (int j = 0; j < recebe; j++) {
            for (int k = 0; k < recebe; k++) {
                if ((j + k == recebe) && (j < k) && !eh_primo(j) && !eh_primo(k)) {
                    resultados[resultado_count][0] = recebe;
                    resultados[resultado_count][1] = j;
                    resultados[resultado_count][2] = k;
                    resultado_count++;
                }
            }
        }
    }

    for (int i = 0; i < qnt_numeros; i++) {
        long int calc_soma = 1000000000;
        bool apareceu = false;
        for (int j = 0; j < resultado_count; j++) {
            if (num_recebe[i] == resultados[j][0]) {
                if (resultados[j][2] - resultados[j][1] < calc_soma) {
                    calc_soma = resultados[j][2] - resultados[j][1];
                    apareceu = true;
                }
            }
        }

        if (!apareceu) {
            printf("-1\n");
        } else {
            for (int j = 0; j < resultado_count; j++) {
                if (num_recebe[i] == resultados[j][0]) {
                    if (resultados[j][2] - resultados[j][1] == calc_soma) {
                        printf("%d %d\n", resultados[j][1], resultados[j][2]);
                        break; // Para evitar múltiplas impressões
                    }
                }
            }
        }
    }

    return 0;
}

