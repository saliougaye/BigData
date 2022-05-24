# [ uova, farina, lievito, zucchero ]

# Magazzino
M = [ 24, 10, 0.1, 3 ]

# Già considero la pasta lievitata all'interno
PA = [ 2, 0.42, 0.014, 0.235 ]
PB = [ 0, 0.6, 0.02, 0.05]
C = [4, 0.5, 0, 0.3]


r = []

def divide_by_zero(v):
    if v == 0:
        return True

    return False


for i in range(0, len(M)):
    
    upa = 0 if divide_by_zero(PA[i]) else M[i] / PA[i]
    upb = 0 if divide_by_zero(PB[i]) else M[i] / PB[i]
    upc = 0 if divide_by_zero(C[i]) else M[i] / C[i]

    r.append([upa, upb, upc])

max = []
for i in range(0, len(r)-1):
    min = 99999999999 # change
    for j in range(0, len(r)):
        if (r[j][i] != 0) & (min > r[j][i]):
            min = r[j][i]
    max.append(min)

ti = []

for i in range(0,4):
    ti.append([PA[i]*max[0], PB[i]*max[1], C[i]*max[2]])


temp = []
for m in range(0,  len(M)):
    p = M[m]

    tot = 0
    for i in ti[m]:
        tot += i
     
    
    temp.append([p, tot])

    
print(temp)