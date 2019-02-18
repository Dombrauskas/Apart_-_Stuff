'''
 ' author Maurício Freire.
 ' Dado um número o programa verifica se este é fatorial 
 ' de algum número.
 ' Given a number the program verifies whether it is the
 ' factorial product of any number.
'''

def rev_fat(fat):
    v = fat
    if fat % 2 != 0:
        return None
        
    for i in range(1,v):
        #print("{}\t/\t{}\t=\t{}".format(fat, i, int(fat / i)))
        
        r = fat % i;
        if (r != 0):
            return None;
        
        fat = int(fat / i)
        if fat == 1:
            return i
        
f = int(input("Digite um número: "))
r = rev_fat(f)
if r is None:
    print(f,"não é fatorial de nenhum número!")
else:
    print("{} é fatorial de {}".format(f,r))
