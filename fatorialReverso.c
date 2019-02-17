/**
 * 
 * autor Mauricio Freire
 * Idem a versão em Python.
 * Idem Python version.
*/

#include <stdio.h>

int rev_fat(int);

int main()
{
    int f, r;
    printf("Digite um numero: ");
    scanf("%d", &f);
    
    r = rev_fat(f);
    if (!r)
        printf("%d nao eh produto fatorial de nenhum numero!\n", f);
    else
        printf("%d eh produto fatorial de %d\n", f, r);
    return 0;
}

int rev_fat(int fat)
{
    int v = fat, i;
    for (i = 1; i < v; i++) {
        fat /= i;
        if (fat == 1) return i;
    }
    return 0;
}
