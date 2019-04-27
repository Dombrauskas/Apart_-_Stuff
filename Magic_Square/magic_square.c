/**
 * 
 * autor Maurício Freire
 * Quadrado Mágico: a soma dos números da primeira linha, da diagonal principal
 * e a da coluna à esquerda devem ser iguais.
 * Magic Square: the sum of the numbers in the first line, the main diagonal and
 * the left column must be the same.
*/
#include <stdio.h>
#include <stdlib.h>

void magic_square(int, int [][*]);

int main()
{
    int n, i, j;
    printf("Qual tamanho de matriz deseja criar?\n");
    scanf("%d", &n);
    int mat[n][n];

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &mat[i][j]);

    magic_square(n, mat);
    return 0;
}

void magic_square(int n, int mat[][n])
{
    int i, j, dia, lin, col;
    dia = lin = col = 0;

    //Soma os valores da 1ª linha, diagonal principal e coluna esquerda.
    //Sum up the values of the 1st line, the main diagonal and left column.
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (i == j) dia += mat[i][j];
            if (j == 0) lin += mat[i][j];
            if (i == 0) col += mat[i][j];
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
    if (dia == lin && lin == col)
        printf("\nMatriz Mágica!\n");
    else printf("\nNope!\n");

    printf("\nSoma da linha superior \t\t= %d\n", lin);
    printf("Soma da diagonal principal \t= %d\n", dia);
    printf("Soma da coluna esquerda \t= %d\n", col);
}
