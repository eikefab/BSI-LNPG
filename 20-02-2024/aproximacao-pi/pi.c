#include <stdio.h>
#include <math.h>

double calc(int length, int index, double agg) {
    if (length == index) {
        return agg;
    }

    int value = (index * 2) + 1;
    double seq = 1 / pow(value, 3);

    if (index == 0) {
        return calc(length, (index + 1), seq);
    }

    if (index % 2 == 0) {
        return calc(length, (index + 1), agg + seq);
    }

    return calc(length, (index + 1), agg - seq);
}

int main() {
    int n;

    printf("Informe o número de termos: ");
    scanf("%d", &n);

    double sequence = calc(n, 0, 0);
    double pi = cbrt(sequence * 32); // Elevar a 1/3 e pegar a raiz cúbica do número é a mesma coisa.

    printf("\n%.5f\n", pi);

    return 0;
}