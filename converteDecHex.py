#
# autor Maurício Freire
#                       Ainda em construção...
#
#

def hex(m):
    print(m)
    a = m
    while a > 15:
        r = a % 16
        if r > 9:
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
            bin.append(r)
        a //= 16

    if m > 15:
        while m > 15:
            m //= 16
            if m > 15:
                hex(m)
            elif m > 9:
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
    elif m > 9:
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

m = (int(input()))#"Digite um número: ")))
bin = []

hex(m)
bin.reverse()
for i in bin:
    print(i, end="")
