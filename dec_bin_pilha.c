/**
 * 
 * autor Maurício Freire
 * Conversor de números decimais em números binário com uso de pilhas.
 * Conversor of decimal numbers to binary number with stack usage.
*/
#include <stdio.h>
#include <stdbool.h>
#define MAX_VET 16

typedef int stack_bin;
// Representação da pilha.
// Stack representation.
typedef struct {
    stack_bin bin[MAX_VET];
    int topo;
} convert;

void stack_init(convert *);
void to_bin(int, convert *);
void push(convert *, int);
stack_bin pop(convert *);
bool stack_isfull(convert);
bool stack_isempty(convert);

int main()
{
    int x;
    convert c;

    do {
        stack_init(&c);

        printf("Digite um numero (decimal): ");
        scanf("%d", &x);

        to_bin(x, &c);
        printf("%d em binario: ", x);

        while (c.topo >= 0)
            printf("%d", pop(&c));
        
        printf("\n\n");
    } while (x >= 0);
    return 0;
}

//Inicializa a pilha.
//Initialize the stack.
void stack_init(convert *c)
{
    c->topo = -1;
}

//Preenche a pilha com os valores 0 e 1.
//Fill the stack with the value 0 and 1.
void to_bin(int n, convert * c)
{
    int r;
    while (n > 0) {
        r = n % 2;
        n /= 2;
        push(c, r);
    }
}

//Preenche a pilha com os valores 0 e 1.
//Fill the stack with the value 0 and 1.
void push(convert * c, int x)
{
    if (!stack_isfull(*c))
        c->bin[++(c->topo)] = x;
    else 
        fprintf(stderr, "Limite excedido!\n\n");
}

//Retorna os valores da pilha.
//Returns values from the stack.
stack_bin pop(convert * c)
{
    if (!stack_isempty(*c))
        return c->bin[c->topo--];
    else {
        fprintf(stderr, "Pilha vazia!\n\n");
        return -1;
    }
}

//Verifica se a pilha está cheia.
//Checks whether the stack is full.
bool stack_isfull(convert c)
{
    return (c.topo == MAX_VET-1);
}

//Verifica se a pilha está vazia.
//Checks whether the stack is empty.
bool stack_isempty(convert c)
{
    return (c.topo == -1);
}
