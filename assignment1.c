#include <stdio.h>
#include <time.h>

#define REPEAT 1000000

void constantTime(int n) {
    volatile int x = n * n;
}

void linearTime(int n) {
    volatile long long sum = 0;
    for(int i = 0; i < n; i++) {
        sum += i;
    }
}

void quadraticTime(int n) {
    volatile long long sum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            sum += i + j;
        }
    }
}

double timeInMs(clock_t start, clock_t end) {
    return ((double)(end - start) * 1000.0) / CLOCKS_PER_SEC;
}

int main() {
    clock_t start, end;

    int sizes[] = {5000, 10000, 20000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("Time Complexity Analysis (ms precision)\n");
    printf("--------------------------------------\n");

    for(int i = 0; i < numSizes; i++) {
        int n = sizes[i];
        printf("\nInput Size n = %d\n", n);

        start = clock();
        for(int k = 0; k < REPEAT; k++)
            constantTime(n);
        end = clock();
        printf("O(1):   %.3f ms\n", timeInMs(start, end));

        start = clock();
        for(int k = 0; k < 10; k++)
            linearTime(n);
        end = clock();
        printf("O(n):   %.3f ms\n", timeInMs(start, end));

        start = clock();
        quadraticTime(n);
        end = clock();
        printf("O(n^2): %.3f ms\n", timeInMs(start, end));
    }

    return 0;
}