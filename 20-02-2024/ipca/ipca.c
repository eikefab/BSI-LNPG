#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct IpcaItem {
    float value;
    int month;
    int year;
} IpcaItem;

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a > b ? b : a;
}

int handle() {
    IpcaItem peak = {};
    IpcaItem bottom = {};

    float agg = 0;
    int computed = 0;

    char ref[255];

    while (strcmp(ref, "*") != 0) {
        fgets(ref, sizeof ref, stdin);
        ref[strcspn(ref, "\n")] = 0;

        if (strcmp(ref, "*") == 0) {
            break;
        }

        char *token = strtok(ref, " ");
        int cursor = 0;

        float value;
        int month;
        int year;

        while (token != NULL) {
            if (cursor == 0) {
                value = atof(token);
            } else if (cursor == 1) {
                month = atoi(token);
            } else {
                year = atoi(token);
            }

            token = strtok(NULL, " ");

            cursor += 1;
        }

        int tmp = month;

        month = min(month, year);
        year = max(tmp, year);
        
        IpcaItem item = {
            .value = value,
            .month = month,
            .year = year
        };

        agg += value;
        computed += 1;

        if (computed == 1) {
            peak = item;
            bottom = item;

            continue;
        }

        if (value > peak.value) {
            peak = item;
        }

        if (value < bottom.value) {
            bottom = item;
        }
    }

    printf("%.2f%% %d/%d\n", peak.value, peak.month, peak.year);
    printf("%.2f%% %d/%d\n", bottom.value, bottom.month, bottom.year);
    printf("%.2f%%\n", (agg / computed));

    return 0;
}

int main() {
    handle();

    return 0;
}
