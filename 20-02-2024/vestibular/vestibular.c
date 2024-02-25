#include <stdio.h>

int getanswers(int *answers) {
    for (int i = 0; i < 10; i++) {
        answers[i] = 10;
    }
}

int main() {
    int answers[10] = {};

    getanswers(*answers);

    for (int i = 0; i < 10; i++) {
        printf("%d", answers[i]);
    } 

    return 0;
}