/**
 * 
 * autor Mauricio Freire
 * Idem a versão em Python.
 * Idem to Python version.
*/
#include <stdio.h>

int rev_fat(int);

int main()
{
    int f, r;
    
    do {
        printf("Digite um numero: ");
        scanf("%d", &f);
        
        r = rev_fat(f);
        if (r == 0)
            printf("%d não é fatorial de nenhum número!\n", f);
        else
            printf("%d é fatorial de %d\n", f, r);
    } while (f > 1);
    return 0;
}

int rev_fat(int fat)
{
    int v, r;
    v = fat;
    // Se o valor for ímpar não é produto fatorial de nenhum número.
    // If the value is odd it is not a factorial product of any number.
    if (fat % 2 != 0) return 0;
    
    for (int i = 1; i <= v; i++) {
        // Se o resto da divisão não for zero o número não fatorial.
        // If the module of the division is not zero it is not factorial.
        r = fat % i;
        if (r != 0) return 0;
        fat /= i;
        if (fat == 1) return i;
    }
    return 0;
}
