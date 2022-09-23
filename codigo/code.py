from cgitb import text


class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def condicionmatriz(lista):
        for elemento in lista:
            sum = 0
            for i in range(len(elemento)):
                if i == 3 and elemento[i] != sum:
                    elemento[i] = sum
                    print("Matriz corregida")
                    print(lista)
                else:
                    sum+=int(elemento[i])
        print("Matriz correcta")
        return lista

    def suma(lista):
        sum = 0
        for elemento in lista:
            for i in elemento:
                sum+=int(i)
        return sum

class Cadenatexto:
    def __init__(self, texto):
        self.texto = texto