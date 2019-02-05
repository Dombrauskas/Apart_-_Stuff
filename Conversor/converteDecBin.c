/**
 * 
 * @autor Mauricio Maurício Freire
 * Mostra a representação binária de um dado número.
 * Shows the binary representation of a chosen number.
*/
#include <stdio.h>

int main()
{
    int i, n = 170;
    int bin[7];

    printf("%d em binario:\n", n);
    for (i = 15; i >= 0; i--) {
        if (n % 2 == 0) {
            bin[i] = 0;
            n = n / 2;
        } else {
            bin[i] = 1;
            n = n / 2;
        }
        if (i % 8 == 0) 
            printf(" ");
    }

    for (i = 0; i <= 7; i++) {
        printf("%d", bin[i]);
    }

    return 0;
}