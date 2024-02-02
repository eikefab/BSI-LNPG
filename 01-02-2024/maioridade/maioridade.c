#include <stdio.h>

int main() {
    int age;

    printf("Insira sua idade: ");
    scanf("%d", &age);

    if (age >= 18) {
        printf("Você é maior de idade.");
    } else {
        printf("Você é menor de idade.");
    }

    printf("\n");

    return 0;
}