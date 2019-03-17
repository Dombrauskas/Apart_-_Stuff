/*
 *
 * author Maurício Freire
 * Cálculo do Máximo Divisor Comum consiste em encontrar o maior termo comum a
 * dois (ou mais) números capaz de dividir ambos.
 * Calcule of the Greatest Common Divisor consists in finding the greatest value
 * common to two (or more) number that is able to divide both.
*/

#include <stdio.h>
#include <stdbool.h>

bool mdc(int, int);

int main()
{
    int s, r, x;
    
    // Impede a escolha de dois números iguais.
    // Prevents the usage of two equal numbers.
    do {
        printf("Informe o primeiro termo: ");
        scanf("%d", &s);
        printf("Informe o segundo termo: ");
        scanf("%d", &r);

        x = mdc(s, r);
    } while (!x);
    return 0;
}

bool mdc(int x, int y)
{
    // Impede a seleção de números iguais ou que um deles seja zero.
    // Prevents the selection of equal numbers or that one of them be zero.
    if ((x == 0 || y == 0) || (x == y)) {
      printf("\nImpossível calcular o MDC\n");
      x = y;
    }
    
    int a, b, mx, mn;
    // Define o maior número.
    // Define the highest number.
    if (x > y) {
        mx = x;
        mn = y;
    } else if (x < y) {
        mx = y;
        mn = x;
    } else {
        printf("Informe números diferentes!\n\n");
        return false;
    }
    
    a = mx / mn;
    b = mx % mn;
    // Se b for diferente de zero o MDC ainda não foi alcançado.
    // If b is non-zero the GCD has not been reached yet.
    if (b != 0)
        mdc(mn, b);
    else
        printf("Mdc %d", mn);
    
    return true;
}
