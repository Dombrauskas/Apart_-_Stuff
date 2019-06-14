"""
 " A ser corrigido
"""

TW = list()
mkp = float()
psc = float()
chm = float()
drs = float()

i = 0

while i < 9:
  vet = [mkp, psc, chm, drs]
  c = 0
  for x in range(4):
    print(x+1,"ª Nota", end=" ")
    vet[x] = float(input())
    c += vet[x]
  TW.append(vet)
  c /= 4
  TW.append(c)
  i += 1

e = 1
for dz in TW:
  media = 0 
  if e == 1:
    print("나연: ", end="")
  if e == 2:
    print("정영: ", end="")
  if e == 3:
    print("사나: ", end="")
  if e == 4:
    print("모모: ", end="")
  if e == 5:
    print("지효: ", end="")
  if e == 6:
    print("미나: ", end="")
  if e == 7:
    print("다현: ", end="")
  if e == 8:
    print("채영: ", end="")
  if e == 9:
    print("쭈의: ", end="")
  e += 1
  media = sum(dz,0)/4
  print(media)
    

