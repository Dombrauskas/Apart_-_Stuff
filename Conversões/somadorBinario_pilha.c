/**
 * 
 * autor Maurício Freire
 * Converte dois números decimais em números binário com uso de pilhas,
 * depois efetua a soma binária dos mesmos.
 * Converts two decimal numbers to binary numbers with stack usage, then
 * showing the binary sum of them both.
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
int stack_size(convert);
void stack_print(convert);

int main()
{
    int x, m = 1, a, p = 0;
    convert c, d, e;

    stack_init(&c); //Guarda 1º valor. | Stores 1st value.
    stack_init(&d); //Guarda 2º valor. | Stores 2nd value.
    stack_init(&e); //Guarda resultado. | Stores the result.

    printf("Digite um numero (decimal): ");
    scanf("%d", &x);
    to_bin(x, &c);

    printf("Digite um numero (decimal): ");
    scanf("%d", &x);
    to_bin(x, &d);

    //Iguala a menor pilha, preenchendo-a com zeros.
    //Evens the fewer stack filling it up with zeros.
    if (stack_size(c) > stack_size(d)) {
        a = stack_size(c) - stack_size(d);
        while (a > 0) {
            push(&d, 0);
            a--;
        }
    } else if (stack_size(c) < stack_size(d)) {
        a = stack_size(d) - stack_size(c);
        while (a > 0) {
            push(&c, 0);
            a--;
        }
    }

    stack_print(c);
    stack_print(d);
    x = 0;
    while (x <= c.topo) {
        a = c.bin[x] + d.bin[x] + p;
        if (a == 2) {
            push(&e, 0);
            p = 1;
        } else if (a == 3) {
            push(&e, 1);
            p = 1;
        } else {
            push(&e, a);
            p = 0;
        }
        ++x;
    }
    /*Se o fim das pilhas forem alcançados e ainda houver um valor a ser
    somado (p = 1), será adicionado aqui.*/
    /*Whether the bottom of the stacks are reached and there is still some
    value to be summed (p = 1), it will be added here.*/
    if (p == 1) push(&e, p);

    printf("________________ +\n");
    while (e.topo >= 0) 
        printf("%d", pop(&e));

    printf("\n\n");
    return 0;
}

//Inicializa a pilha.
//Initialize the stack.
void stack_init(convert * c)
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

//Calcula o tamanho de uma pilha.
//Calculates the size of a stack.
int stack_size(convert c)
{
    if (!stack_isempty(c)) {
        int s = 1, i;
        for (i = 0; i < c.topo; i++)
            s++;
        return s;
    }
    return 0;
}

//Exibe o conteúdo da pilha.
//Displays the stack content.
void stack_print(convert c)
{
    while (c.topo >= 0)
        printf("%d", c.bin[c.topo--]);
    printf("\n");
}
