#
# autor Maurício Freire
#                       Ainda em construção...
#
#

m = (int(input()))#"Digite um número: ")))
bin = []

'''
while m > 0:
    if m > 16:
        m //= 16
    elif m % 16 >= 10:
        if m == 10:
            bin.append('A')
        if m == 11:
            bin.append('B')
        if m == 12:
            bin.append('C')
        if m == 13:
            bin.append('D')
        if m == 14:
            bin.append('E')
        if m == 15:
            bin.append('F')
    else:
        bin.append(m)

for i in bin:
    print(i, end="")
'''

while m > 0:
    if m > 16:
        m //= 16
    print(m)
