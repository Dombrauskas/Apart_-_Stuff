pneu = 100

def desg(pneu, desgaste):
    count = 0
    while (pneu >= 38):
        pneu = pneu - (pneu * desgaste)
        count += 1
    
    return count


print("Total de voltas possíveis no SS:", desg(pneu, 0.09))
print("Total de voltas possíveis no  S:", desg(pneu, 0.04))
print("Total de voltas possíveis no  M:", desg(pneu, 0.03))

