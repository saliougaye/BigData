
# polinomi rappresentati da array, dal coifficiente più basso al più alto
# q = [-1, 1, 2, 0, 1, 0] # x^4 + 2x^2 + x - 1
# p = [1, 1, 1] # x^2 + x + 1

def remove_zero(poly):
    # tolgo i valori con coefficiente 0, per stampargli meglio
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def div(poly1, poly2):
    # se il secondo polinomio ha grado maggiore del primo ritornare resto 0 con il poly1
    if len(poly2) > len(poly1):
        return [0], poly1

    # prendo la differenza di lunghezza per avere la stessa lunghezza di poly2
    l = len(q) - len(p)

    poly2 = [0] * l + poly2

    result = []
    # eseguo la divisione in colonna ciclata
    for _ in range(l+1):
        m = poly1[-1] / float(poly2[-1])

        result = [m] + result

        if m != 0:
            d = [m * u for u in poly2]
            poly1 = [u - v for u, v in zip(poly1, d)]

        poly1.pop()
        poly2.pop(0)
    
    remove_zero(poly1)
    remove_zero(result)

    return result, poly1


def print_poly(poly):
    p = []
    print(poly)
    for i, v in enumerate(poly):
        if i == 0:
            p.append('{0:+}'.format(v))
        elif (i == 1):
            if v == 1:
                p.append('x')
            else:
                p.append('{0:+}x'.format(v))
        else:
            if v == 1:
                p.append(f'x^{i}')
            else:
                s = '{0:+}'.format(v)
                p.append(f'{s}x^{i}')

    p.reverse()
    print(''.join([f'{item} ' for item in p]))



def input_list():
    n = int(input("Number of elements: "))
    list = []
    for _ in range(0,n):
        list.append(float(input("Insert number: ")))

    return list

print("Insert first polynomial")
q = input_list()
print("Insert second polynomial")
p = input_list()
res, rem = div(q, p)
print_poly(res)