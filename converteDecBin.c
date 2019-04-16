/**
 * 
 * @autor Maurício Freire
 * Mostra a representação binária de um dado número.
 * Shows the binary representation of a chosen number.
*/
#include <stdio.h>

int main()
{
    int i, n;
    int bin[16];

    printf("Informe um numero (decimal): ");
    scanf("%d", &n);
    
    printf("%d em binario:\n", n);
    for (i = 15; i >= 0; i--) {
        if (n % 2 == 0)
            bin[i] = 0;
        else
            bin[i] = 1;
        n /= 2;
    }

    for (i = 0; i < 16; i++) {
        printf("%d", bin[i]);
        if (i % 8 == 0) printf(" ");
    }
    return 0;
}
