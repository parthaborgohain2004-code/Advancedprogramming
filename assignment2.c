#include <stdio.h>
#include <stdlib.h>
void constantSpace(int n) {
int x = 10;
int y = 20;
int sum = x + y;
printf("Constant Space Used: %lu bytes\n", sizeof(x) + sizeof(y) + sizeof(sum));
}
void linearSpace(int n) {
int *arr = (int *)malloc(n * sizeof(int));
if (arr == NULL) {
printf("Memory Allocation Failed\n");
return;
}
printf("Linear Space Used for n=%d: %lu bytes\n", n, n * sizeof(int));
free(arr);
}
void quadraticSpace(int n) {
int **matrix = (int **)malloc(n * sizeof(int *));
for (int i = 0; i < n; i++) {
matrix[i] = (int *)malloc(n * sizeof(int));
}
printf("Quadratic Space Used for n=%d: %lu bytes\n", n, (unsigned long)(n * n * sizeof(int)));
for (int i = 0; i < n; i++) {
free(matrix[i]);
}
free(matrix);
}
int main() {
int n;

printf("Enter value of n: ");
scanf("%d", &n);
printf("\n--- Space Complexity Analysis ---\n");
constantSpace(n);
linearSpace(n);
quadraticSpace(n);
return 0;
}