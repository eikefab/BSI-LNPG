#include <stdio.h>

int main() {
    int a, b;

    printf("Informe dois números inteiros: ");
    scanf("%d %d", &a, &b); // Permite receber N inteiros de uma só vez, assim, basta informar-los no formato <inteiro 1> <inteiro 2>.

    printf("%d + %d = %d\n", a, b, (a + b));
    printf("%d - %d = %d\n", a, b, (a - b));
    printf("%d * %d = %d\n", a, b, (a * b));
    printf("%d / %d = %f\n", a, b, ((float) a / b));

    return 0;
}