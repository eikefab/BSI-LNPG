#include <stdio.h>

/** 
 * Optei por uma abordagem diferente e não usar 6 variáveis (3 notas, 3 pesos)
 * assim, por mais que seja um pouco de overengineering, ficou "mais limpo" na minha opinião,
 * apesar de mais lento (por usar 2 loops), esse impacto é irrelevante, uma vez que são loops pequenos.
*/

typedef struct Nota {
    float valor;
    int peso;
} Nota;

int main() {
    Nota notas[3] = {};

    for (int i = 0; i < 3; i++) {
        float nota;
        int peso;

        printf("Insira a nota e seu peso (%dº): ", (i + 1));
        scanf("%f %d", &nota, &peso);

        Nota dados = {
            .peso = peso,
            .valor = nota
        };

        notas[i] = dados;
    }

    int pesoTotal = 0;
    float total = 0;

    for (int i = 0; i < 3; i++) {
        Nota nota = notas[i];

        pesoTotal += nota.peso;
        total += (nota.valor * nota.peso);
    }

    float media = total / pesoTotal;

    printf("Média total: %.2f\n", media);

    return 0;
}