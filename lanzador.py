from codigo.code import Matriz, Cadenatexto, Generadorlista, ScriptTabla

def separador():
    print("--------------------------------------------------------")

def ejecutar():
    matriz = Matriz([[1,1,1,3],[2,2,2,7],[3,3,3,9],[4,4,4,13]]).matriz
    Matriz.condicionmatriz(matriz)
    separador()
    suma = Matriz.suma(matriz); print(f"La función suma devuelve una suma de todos los elementos de la lista, que en este caso es igual a {suma}.")
    separador()
    texto = Cadenatexto("Me llamo Javier").texto
    comprobar = Cadenatexto.comprobarlonguitud(texto)
    print(comprobar); separador()
    l1,l2,l3,l4,l5 = Generadorlista.generarlista()
    print(l1, l2, l3, l4, l5); separador()
    ScriptTabla.scripttabla()