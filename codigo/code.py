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

    def comprobarlonguitud(cadena):
        if 3<= len(cadena) >= 10:
            print("La cadena está entre 3 y 10 caracteres.")
            return True
        else:
            print("La cadena no está entre los 3 y 10 caracteres.")
            return False