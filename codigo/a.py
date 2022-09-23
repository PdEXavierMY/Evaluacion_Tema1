def generarnumero(n, lista1, condicion, sumatorio):
        if n!=condicion:
            lista1.append(n)
            n+=sumatorio
            generarnumero(n, lista1, condicion, sumatorio)
        else:
            print(lista1)

generarnumero(0, [], 22, 2)