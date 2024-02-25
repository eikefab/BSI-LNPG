#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Student {
    char name[255];
    int score;
} Student;

int len(int a[255]) {
    int i = 0;

    for (int j = 0; j < 255; j++) {
        int k = a[j];

        if (k == -1) {
            continue;
        }

        i += 1;
    }

    return i;
}

int matchAnswers(int origin[255], int compare[255]) {
    int originLength = len(origin);
    int compareLength = len(compare);

    if (originLength != compareLength) {
        return -1;
    }

    int match = 0;

    for (int i = 0; i < originLength; i++) {
        int a = origin[i];
        int b = compare[i];

        if (a == b) {
            if (a == -1) {
                continue;
            }

            match += 1;
        }
    }

    return match;
}

int *fetchAnswers() {
    static int *answers;
    answers = malloc(255 * sizeof(int));

    for (int i = 0; i < 255; i++) {
        answers[i] = -1;
    }

    char line[255];

    fgets(line, sizeof line, stdin);
    line[strcspn(line, "\n")] = 0;

    char *token = strtok(line, " ");
    int cursor = 0;

    while (token != NULL) {
        answers[cursor] = atoi(token);

        token = strtok(NULL, " ");
        cursor += 1;
    }

    return answers;
}

Student *fetchStudents(int correct[255]) {
    static Student *students;
    students = malloc(255 * sizeof(Student));

    for (int i = 0; i < 255; i++) {
        strcpy(students[i].name, "");
        students[i].score = -1;
    }

    char name[255];

    fgets(name, sizeof name, stdin);
    name[strcspn(name, "\n")] = 0;

    int cursor = 0;

    while (strcmp(name, "*") != 0) {
        int *answers = fetchAnswers();

        int score = matchAnswers(answers, correct);

        free(answers);

        strcpy(students[cursor].name, name);
        students[cursor].score = score;

        fgets(name, sizeof name, stdin);
        name[strcspn(name, "\n")] = 0;

        cursor += 1;
    }

    return students;
}

Student topStudent(Student students[255]) {
    Student student = {};
    int score = 0;

    for (int i = 0; i < 255; i++) {
        Student comparison = students[i];

        if (comparison.score > score) {
            student = comparison;
            score = comparison.score;
        }
    }

    return student;
}

Student bottomStudent(Student students[255], int topScore) {
    Student student = {};
    int score = topScore;

    for (int i = 0; i < 255; i++) {
        Student comparison = students[i];

        if (comparison.score == -1) {
            continue;
        }

        if (score > comparison.score) {
            student = comparison;
            score = comparison.score;
        }
    }

    return student;
}

float getPercentage(int answers[255], Student students[255]) {
    int count = 0;
    int total = 0;

    for (int i = 0; i < 255; i++) {
        Student student = students[i];

        if (student.score == -1) {
            continue;
        }

        total += 1;

        if (student.score > (len(answers) / 2)) {
            count += 1;
        }
    }

    return (count / (float) total) * 100;
}

void handle() {
    int *answers = fetchAnswers();
    Student *students = fetchStudents(answers);

    Student top = topStudent(students);
    Student bottom = bottomStudent(students, top.score);

    printf("%s: %d\n", top.name, top.score);
    printf("%s: %d\n", bottom.name, bottom.score);
    printf("%.2f%% acertaram mais da metade.\n", getPercentage(answers, students));

    free(answers);
    free(students);
}

int main() {
    handle();

    return 0;
}