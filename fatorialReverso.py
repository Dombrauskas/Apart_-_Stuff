# Dado um número o programa verifica se este é fatorial 
# de algum número.
# Given a number the program verifies whether it is the
# factorial product of any number.

def rev_fat(fat):
    v = fat
    for i in range(1,v):
        while fat > i:
            print("{}\t/\t{}\t=\t{}".format(fat, i, int(fat / i)))
            fat = int(fat / i)
            if fat == 1:
                return i
        
f = int(input())
r = rev_fat(f)
if r == None:
    print(f,"não é fatorial de nenhum número!")
else:
    print("{} é fatorial de {}".format(f,r))
