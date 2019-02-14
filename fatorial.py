# Calcula o fatorial de um número.
# Calculates the fatorial of a number.

def Fatorial(fat):
	if (fat == 1):
	    return 1
	return fat * Fatorial(fat - 1)

n = (int(input("Digite um número: ")))

print("Fatorial de {} é: {}".format(n,Fatorial(n)))
