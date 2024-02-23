#include <stdio.h>
#include <math.h>

double calc(int lenght, int index, int value, double agg) {
    if (lenght == index) {
        return agg;
    }

    double seq = 1 / pow(value, 3);

    if (index == 0) {
        return calc(lenght, (index + 1), (value + 2), seq);
    }

    if (index % 2 == 0) {
        return calc(lenght, (index + 1), (value + 2), agg + seq);
    }

    return calc(lenght, (index + 1), (value + 2), agg - seq);
}

int main() {
    int n;

    printf("Informe o número de termos: ");
    scanf("%d", &n);

    double sequence = calc(n, 0, 1, 0);
    double pi = cbrt(sequence * 32); // Elevar a 1/3 e pegar a raiz cúbica do número é a mesma coisa.

    printf("\n%.5f\n", pi);

    return 0;
}