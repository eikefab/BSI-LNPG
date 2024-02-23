#include <stdio.h>
#include <string.h>

int handlePassenger(int current, int pax) { // A consertar
    if (current == pax) {
        return 0;
    }

    char rg[255], birthdate[255], ticket[255], ticketBirthdate[255], ticketSeat[255];

    printf("\nPassageiro %d:\n", (current + 1));
    printf("RG (ou 'Nao possui'): ");

    fgets(rg, sizeof rg, stdin);
    rg[strcspn(rg, "\n")] = 0;

    puts(rg);
    printf("%d", strcmp(rg, "Nao possui"));

    if (strcmp(rg, "Nao possui") == 0) {
        printf("\nA saída é nessa direção.\n");

        return handlePassenger((current + 1), pax);
    }

    printf("Data de nascimento (RG): ");
    scanf("%s", birthdate);

    printf("Passagem (ou 'Nao possui'): ");
    
    fgets(ticket, sizeof ticket, stdin);
    ticket[strcspn(rg, "\n")] = 0;

    puts(ticket);
    printf("%d", strcmp(ticket, "Nao possui"));

    if (strcmp(ticket, "Nao possui") == 0) {
        printf("\nA recepção é nessa direção.\n");

        return handlePassenger((current + 1), pax);
    }

    printf("Data de nascimento (Passagem): ");
    scanf("%s", ticketBirthdate);

    if (strcmp(birthdate, ticketBirthdate) != 0) {
        printf("\n190\n");

        return handlePassenger((current + 1), pax);
    }

    printf("Assento (ex.: A12): ");
    scanf("%s", ticketSeat);
    getchar();

    printf("O seu assento é %s, tenha um ótimo dia.\n", ticketSeat);

    return handlePassenger((current + 1), pax);
}

int main() {
    int pax;

    printf("\nQuantidade de passageiros: ");
    scanf("%d", &pax);
    getchar();

    handlePassenger(0, pax);

    return 0;
}