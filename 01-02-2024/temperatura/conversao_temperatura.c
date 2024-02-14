#include <stdio.h>

float fahrenheit(int celsius) {
    return (celsius * 1.8) + 32;
}

int main() {
    int celsius;

    printf("Informe a temperatura em ºC: ");
    scanf("%d", &celsius);

    printf("%dºC é equivalente a %.2fºF\n", celsius, fahrenheit(celsius));

    return 0;
}