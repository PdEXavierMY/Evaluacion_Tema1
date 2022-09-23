class Matriz:
    def __init__(self):
        self.matriz = [[1,1,1,3],[2,2,2,7],[3,3,3,9],[4,4,4,13]]

    def condicionmatriz(lista):
        sum = 0
        for elemento in lista:
            for i in range(len(elemento)):
                if i == 3:
                    if elemento[i] == sum:
                        print("Matriz correcta")
                    else:
                        elemento[i] = sum
                        print("Matriz corregida")
                        print(lista)
                else:
                    sum+=int(elemento[i])
        return lista

    def suma(lista):
        sum = 0
        for elemento in lista:
            for i in elemento:
                sum+=int(i)
        return sum

matriz = [[1,1,1,3],[2,2,2,7],[3,3,3,9],[4,4,4,13]]
Matriz.condicionmatriz(matriz)