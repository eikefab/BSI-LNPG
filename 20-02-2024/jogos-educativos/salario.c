#include <stdio.h>

float gettotal(float price, int sold) {
    return price * sold;
}

float getwage(float total, float bonus) {
    return (total / 2) + bonus;
}

float calcbonus(float actual, float agg, int times, int index) {
    if (times == index) {
        return agg;
    }

    return calcbonus(actual * 0.92, agg + (actual * 0.08), times, (index + 1));
}

float getbonus(float total, int sold) {
    int times = sold / 15;

    if (times == 1) {
        return total * 0.08;
    }

    return calcbonus(total, 0, times, 0);
}

int main() {
    float price = 19.9;
    int sold;

    printf("Informe o número de vendas: ");
    scanf("%d", &sold);

    float total = gettotal(price, sold);
    float bonus = getbonus(total, sold);
    float wage = getwage(total, bonus);

    printf("%.2f\n", total);
    printf("%.2f\n", bonus);
    printf("%.2f\n", wage);

    return 0;
}