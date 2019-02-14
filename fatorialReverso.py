# Não acabado ainda!!!

def Fatorial(fat):
    for i in range(2,fat):
        fat /= i
        if (fat == i):
            return f
        else:
            Fatorial(int(fat))

n = (int(input("Digite um número: ")))

f = Fatorial(n)

print(f)
