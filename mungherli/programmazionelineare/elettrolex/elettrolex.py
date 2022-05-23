# Produzione
PI = 2000
PE = 600

# Costi
CI = 100
CE = 150
CM = 2


GI = 300 # Giacenza Iniziale
GF = 300 # Giacenza Finale

V = [1200, 2100,2400,3000,4000] # Vendite nei 5 mesi


def main():
    """start"""

    # Partiamo dall'ultimo mese
    V.reverse()

    # Aggiungiamo la giancenza finale all'ultimo mese
    V[0] = V[0] + GF

    # unita in magazzino nel mese precedente
    u = abs(PI + PE - V[0])

    r = [u] # unita in magazzino per mese

    for v in range(1, len(V)):
        
        u = u - PI - PE + V[v]

        # print(V[v],u)
        r.append(u)
        
    # li metto in ordine di mese
    r.reverse()

    r[0] = r[0] + GI

    # rimetto l'ordine dall'ultimo mese
    V.reverse()


    # eseguo i calcoli al contrario
    for u in range(1, len(r)):
        pt = - r[u-1] + V[u-1] + r[u]

        x = PI - pt
        y = 0

        if x < 0:
            y = PE + x
            x = PI

            if y == 0:
                y = PE
            

        print(f'x({u}) = {x}', f'y({u}) = {y}')

    # l'ultimo calcolo devo aggiungere anche la giacenza finale
    pt = V[len(V)-1] + GF - r[len(r)-1]

    x = PI - pt
    y = 0

    if x < 0:
        y = PE + x
        x = PI

        if y <= 0:
            y = PE


        

    print(f'x({len(V)}) = {x}', f'y({len(V)}) = {y}')




main()