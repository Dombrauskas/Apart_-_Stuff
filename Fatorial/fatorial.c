/**
 * 
 * autor Maurício Freire
 * Calcula o fatorial de um número.
 * Calculates the fatorial of a number.
*/
#include <stdio.h>

int fatorial(int);

int main()
{
    int f;
    printf("Digite um numero: ");
    scanf("%d", &f);
    printf("%d\n", fatorial(f));
    return 0;
}

int fatorial(int f)
{
    if (f == 1) return 1;
    return f * fatorial(f - 1);
}
