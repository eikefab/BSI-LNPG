# include <stdio.h>

int main() {
    int a;

    printf("Informe um inteiro: ");
    scanf("%d", &a);

    if (a % 2) {
        printf("%d é par.\n", a);
    } else {
        printf("%d é ímpar.\n", a);
    }

    return 0;
}