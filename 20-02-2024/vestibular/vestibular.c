#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void getanswers(int *answers[10]) {
    char ref[255];

    fgets(ref, sizeof ref, stdin);
    ref[strcspn(ref, "\n")] = 0;

    char *token = strtok(ref, " ");
    int cursor = 0;

    while (token != NULL) {
        int value = atoi(token);
        answers[cursor] = value;

        token = strtok(NULL, " ");
        cursor += 1;
    }
}

void getstudents(char *names[255][255], int *scores[255], int correct[10]) {
    char name[255];

    fgets(name, sizeof name, stdin);
    name[strcspn(name, "\n")] = 0;

    int cursor = 0;

    while (strcmp(name, "*") != 0) {
        int answers[10] = {};

        getanswers(&answers);

        strcpy(names[cursor], name);
        scores[cursor] = match(correct, answers);

        cursor += 1;

        fgets(name, sizeof name, stdin);
        name[strcspn(name, "\n")] = 0;
    }
}

int match(int correct[10], int answers[10]) {
    int i = 0;

    for (int j = 0; j < 10; j++) {
        int k = correct[j];
        int l = answers[j];

        if (k == l) {
            if (k == 0) {
                continue;
            }

            i += 1;
        }
    }

    return i;
}

int studentslen(int scores[255]) {
    int len = 0;

    for (int i = 0; i < sizeof scores; i++) {
        if (scores[i] == -1) {
            continue;
        }

        len += 1;
    }

    return len;
}

int topindex(char names[255][255], int scores[255]) {
    int temp = 0;
    int cursor = 0;

    int len = studentslen(names);

    for (int i = 0; i < len; i++) {
        int score = scores[i];

        if (score > temp) {
            temp = score;
            cursor = i;
        }
    }

    return cursor;
}

int botindex(char names[255][255], int scores[255], int topindex) {
    int temp = scores[topindex];
    int cursor = topindex;

    int len = studentslen(names);

    for (int i = 0; i < len; i++) {
        int score = scores[i];

        if (score < temp) {
            temp = score;
            cursor = i;
        }
    }

    return cursor;
}

int main() {
    int correct[10] = {};

    char names[255][255];
    int scores[255];

    for (int i = 0; i < sizeof scores; i++) {
        scores[i] = -1;
    }

    getanswers(&correct);
    getstudents(&names, &scores, correct);

    for (int i = 0; i < sizeof scores; i++) {
        printf("%d\n", scores[i]);
    }

    int topStudent = topindex(names, scores);
    int botStudent = botindex(names, scores, topStudent);

    printf("%s: %d", names[topStudent], scores[topStudent]);
    printf("%s: %d", names[botStudent], scores[botStudent]);

    return 0;
}