from codigo.code import Matriz, Cadenatexto, Generadorlista, ScriptTabla, Codewars
from introducir import solicitar_introducir_numero_extremo2

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
    separador()

def ejecutar2():
    eleccion = solicitar_introducir_numero_extremo2("¿Qué ejercicio quieres runnear?", 1, 5)
    if eleccion == 3:
        Generadorlista.generarnumero(0, [], 11, 1)
        Generadorlista.generarnumero(-10, [], 1, 1)
        Generadorlista.generarnumero(0, [], 21, 2)
        Generadorlista.generarnumero(-19, [], 0, 2)
        Generadorlista.generarnumero(0, [], 51, 5)
    elif eleccion == 5:
        Codewars.string_to_array(input("Introduce una cadena de texto: "))
