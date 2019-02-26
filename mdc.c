/*
 *
 * author Maurício Freire
 * Cálculo do Máximo Divisor Comum consiste em encontrar o maior termo comum a
 * dois (ou mais) números capaz de dividir ambos.
 * Calcule of the Greatest Common Divisor consists in finding the greatest value
 * common to two (or more) number that is able to divide both.
*/

#include <stdio.h>

void mdc(int, int);

int main()
{
    int s, r;
    
    // Impede a escolha de dois números iguais.
    // Prevents the usage of two equal numbers.
    do {
        printf("Informe o primeiro termo: ");
        scanf("%d", &s);
        printf("Informe o segundo termo: ");
        scanf("%d", &r);
        
        mdc(s,r);
    } while (s == r);
    return 0;
}

void mdc(int x, int y)
{
    int a, b, mx, mn;
    // Define o maior número.
    // Define the highest number.
    if (x > y) {
        mx = x;
        mn = y;
    } else if (x < y) {
        mx = y;
        mn = x;
    } else 
        printf("Informe números diferentes!");
    
    a = mx / mn;
    b = mx % mn;
    //printf("%d / %d = %d", mx, mn, b);
    // Se b for diferente de zero o MDC ainda não alcançado.
    // If b is non-zero the GCD has not been reached yet.
    if (b != 0)
        mdc(mn, b);
    else
        printf("Mdc %d", mn);
}
