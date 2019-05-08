/**
 * 
 * autor Maurício Freire
 * Exibe a sequênicia de Finabonacci até um dado número.
 * Shows the Finabonacci sequence until a given number.
*/

#include <stdio.h>

int fibonacci(int);
void fib(int);

int main()
{
    int x;
    printf("Informe um numero: ");
    scanf("%d", &x);
    fib(x);
    //printf("%d ", fibonacci(x));
    return 0;
}

/*
int fibonacci(int x)
{
    if (x < 2) 
        return x;
    else
        return fibonacci(x-1) + fibonacci(x-2);
}
*/

void fib(int x)
{
    int a, b, c;
    a = b = c = 1;
    while (c <= x) {
        if (b == 1)
            printf("%d %d ", a, b);
        c = b + a;
        a = b;
        b = c;
        printf("%d ", c);
    }
}
