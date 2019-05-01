/**
 *                                          AINDA EM ANDAMENTO!
 * autor Maurício Freire
 * Quadrado Mágico: a soma dos números da primeira linha, da diagonal principal
 * e a da coluna à esquerda devem ser iguais.
 * Magic Square: the sum of the numbers in the first line, the main diagonal and
 * the left column must be the same.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void magic_square(int, int [][*]);
int alakazan(int *, int *, int, int, int[][*]);

int main()
{
    int n, i, j;
    printf("Qual tamanho de matriz deseja criar?\n");
    scanf("%d", &n);
    int mat[n][n];

    for (i = 0; i < n; i++)
        //for (j = 0; j < n; j++)
        do {
            printf("[0 - 9] -> ");
            scanf("%d", &mat[0][i]);
        } while(mat[0][i] < 0 || mat[0][i] > 9);

    magic_square(n, mat);
    return 0;
}

void magic_square(int n, int mat[][n])
{
    int i, j, dia, lin, col, e = 0;
    lin = 0;

    //Preenche a parte não digitada pelo usuário da matriz.
    //Fill up the unfilled part of the matrix by the user.
    srand(time(NULL));
    j = 1;
    while (j < n) {
        for (i = 0; i < n; i++)
            mat[j][i] = rand() % 9;
        j++;
    }
    
    for (i = 0; i < n; i++)
        lin += mat[0][i];

    //Soma os valores da 1ª linha, diagonal principal e coluna esquerda.
    //Sum up the values of the 1st line, the main diagonal and left column.
    do {
        col = dia = 0;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (i == j) dia += mat[i][j];
                if (j == 0) col += mat[i][j];
                printf("%d ", mat[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        printf("%2d %2d %2d\n", col, dia, lin);
        if (col != dia && col != lin) e = alakazan(&col, &dia, lin, n, mat);
    } while (e == 0);

    if (dia == lin && lin == col)
        printf("\nMatriz Mágica!\n");
    else printf("\nNope!\n");

    printf("\nSoma da linha superior \t\t= %d\n", lin);
    printf("Soma da diagonal principal \t= %d\n", dia);
    printf("Soma da coluna esquerda \t= %d\n", col);
}

//Corrige os números da matriz.
//Fix the matrix numbers up.
int alakazan(int *col, int *dia, int lin, int n, int mat[][n])
{
    int i = 1, j = 1, x;

    x = lin - *col;
    while (0 < 10) {
        mat[n-i][0] += x;
        if (mat[n-i][0] > 9) {
            x = mat[n-i][0] - 9;
            mat[n-i][0] -= x;
        } else if (mat[n-i][0] < 0) {
            mat[n-i][0] += -x;
        } else break;
        i++;
        if (i ==n - 1) i = 1;
        /*
        if (i == n - 1) {
            i = 1;
            if (x % 2 == 0) x %= (n - 1);
            for (i = 1; i < n - 1; i++)
                mat[n-i][0] -= x;
            mat[n-i][0] -= (x + 1);
        }*/
    }

    x = lin - *dia;
    while (0 < 10) {
        mat[n-j][n-j] += x;
        if (mat[n-j][n-j] > 9) {
            x = mat[n-j][n-j] - 9;
            mat[n-j][n-j] -= x;
        } else if (mat[n-j][n-j] < 0) {
            mat[n-j][n-j] += -x;
        } else break;
        j++;
        if (j == n - 1) j = 1;
    }

    printf("\n");
    *col = *dia = 0;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (j == 0) *col += mat[i][j];
            if (i == j) *dia += mat[i][j];
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    return 1;
}
