from code import Matriz, Cadenatexto

matriz = Matriz([[1,1,1,3],[2,2,2,7],[3,3,3,9],[4,4,4,13]]).matriz
Matriz.condicionmatriz(matriz)
suma = Matriz.suma(matriz); print(f"La función suma devuelve una suma de todos los elementos de la lista, que en este caso es igual a {suma}.")
texto = Cadenatexto("Me llamo Javier").texto
comprobar = Cadenatexto.comprobarlonguitud(texto)
print(comprobar)