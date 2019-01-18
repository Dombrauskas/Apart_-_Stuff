/*
 *
 * autor Maurício Freire
 * A Conjectura de Goldbach diz que todo número par maior que 2 pode ser obtido pela
 * soma de dois números primos inferiores a ele.
 * The Goldbach's Conjecture says that any even number greater than 2 may be written
 * as the sum of two prime numbers.
*/

#include <stdio.h>
#include <string.h>

void nums_prims(int);
void Goldbach(int*, int);

int main()
{
    int x;
    printf("Digite um numero: ");
    scanf("%d", &x);
    nums_prims(x);
    return 0;
}

/*
 * Preenche um vetor com todos os números primos dentro do limite escolhido.
 * Fill an array with all the prime numbers within the boundaries chosen.
*/
void nums_prims(int a)
{
    int i, j, p = 0, v[a/2], c = 0, u;
    for (i = 1; i <= a; i++) {
        for (j = 1; j <= i; j++)
            if (i % j == 0) p++;
        
        if (p <= 2) v[c++] = i;
        p = 0;
    }
    
    printf("Numeros primos entre 1 e %d:\n", a);
    for (i = 0; v[i] != '\0'; i++)
        printf("Numero primo #%02d: %d\n", i+1, v[i]);
        
    printf("Digite um numero par: ");
    scanf("%d", &u);
    //Se o número for ímpar ele será decrementado antes de ser passado para a função.
    //If the number is odd it shall be decremented before being passed to the function.
    if (u % 2 == 0) Goldbach(v, u);
    else Goldbach(v, --u);
}

/*
 * Função para encontrar uma soma possível (pode haver mais de uma) de
 * primos para formar a expressão.
 * Function to encounter a possible sum (there might have plus than one)
 * of primes to make the expression.
*/
void Goldbach(int *s, int g)
{
    printf("\n");
    int i, j, k;
    for (i = 0; i < g; i ++)
        if (s[i] > g) break;
    
    //Mostra as possibilidades de soma entre primos para resultar no número par escolhido.
    //Shows the possible sums between primes that result in the chosen even number.
    for (j = i; j >= 0; j--) 
        for (k = 0; k < i; k++) 
            if (s[j] + s[k] == g) 
                printf("%d + %d = %d\n", s[k], s[j], g);
    
}
