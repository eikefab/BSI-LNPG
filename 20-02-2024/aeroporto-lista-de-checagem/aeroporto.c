#include <stdio.h>
#include <string.h>

int handlepax(int current, int pax) {
    if (current == pax) {
        return 0;
    }

    char rg[255], birthdate[255], ticket[255], ticketBirthdate[255], ticketSeat[255];

    printf("\nPassageiro %d:\n", (current + 1));
    printf("RG (ou 'Nao possui'): ");

    fgets(rg, sizeof rg, stdin);
    rg[strcspn(rg, "\n")] = 0;

    if (strcmp(rg, "Nao possui") == 0) {
        printf("\nA saída é nessa direção.\n");

        return handlepax((current + 1), pax);
    }

    printf("Data de nascimento (RG): ");
    scanf("%s", birthdate);
    getchar();

    printf("Passagem (ou 'Nao possui'): ");
    
    fgets(ticket, sizeof ticket, stdin);
    ticket[strcspn(ticket, "\n")] = 0;

    if (strcmp(ticket, "Nao possui") == 0) {
        printf("\nA recepção é nessa direção.\n");

        return handlepax((current + 1), pax);
    }

    printf("Data de nascimento (Passagem): ");
    scanf("%s", ticketBirthdate);

    if (strcmp(birthdate, ticketBirthdate) != 0) {
        printf("\n190\n");

        return handlepax((current + 1), pax);
    }

    printf("Assento (ex.: A12): ");
    scanf("%s", ticketSeat);
    getchar();

    printf("O seu assento é %s, tenha um ótimo dia.\n", ticketSeat);

    return handlepax((current + 1), pax);
}

int main() {
    int pax;

    printf("\nQuantidade de passageiros: ");
    scanf("%d", &pax);
    getchar();

    handlepax(0, pax);

    return 0;
}