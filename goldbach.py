# Idem ao anteriores.
# Equal to the others.
    
def primos(p):
    x = 0
    c = x
    v = []
    for n in range(1,p+1):
        for j in range(1,p+1):
            if n % j == 0:
                x += 1
        if x <= 2:
            v += [n]
        x = 0
    print("Números primos entre 1 e", p,":")
    print(v)
    Goldbach(v, p)

def Goldbach(v, p):
    flag = False
    g = (int(input("\nDigite um número inferior a ")))
    print(p, ">>>", g)
    
    for i in range(g):
        if v[i] > g:
            break
        
    for j in range(0,i):
        for k in range(0,i+1):
            if v[j] + v[k] == g:
                print(v[j], "+", v[k], "=", g)
    
p = (int(input("Digite um número: ")))
print(p,"\n")
primos(p)
