#include <stdio.h>

char getId() {
    char id;

    printf("Digite a operação (+, -, *, /): ");
    scanf("%c", &id);

    return id;
}

float getNumber(int index) {
    printf("Digite o %dº número: ", index);

    float num;
    scanf("%.2f", &num);

    return num;
}

float getFirstNumber() {
    return getNumber(1);
}

float getSecondNumber() {
    return getNumber(2);
}

void sum(float a, float b) {
    printf("%.2f\n", (a + b));
}

void sub(float a, float b) {
    printf("%.2f\n", (a - b));
}

void mult(float a, float b) {
    printf("%.2f\n", (a * b));
}

void div(float a, float b) {
    if (b == 0) {
        printf("Divisão por zero.");

        return;
    }

    printf("%.2f\n", (a / b));
}

void handle(char id, float a, float b) {
    switch (id) {
        case '+':
            sum(a, b);

            break;
        case '-':
            sub(a, b);

            break;
        case '*':
            mult(a, b);

            break;
        case '/':
            div(a, b);

            break;
        default:
            printf("Operação inválida.");

            break;
    }
}

int main() {
    char id = getId();
    float a = getFirstNumber();
    float b = getSecondNumber();

    handle(id, a, b);
}