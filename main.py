# main.py
# Punto de entrada del programa.

from diccionario import obtener_definicion
from practicas import obtener_pregunta

def menu():
    print("=== Asistente Educativo ===")
    print("1. Buscar definición")
    print("2. Obtener pregunta de práctica")
    print("3. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        termino = input("Escribe el término que deseas buscar: ")
        print("Definición:", obtener_definicion(termino))
    elif opcion == "2":
        print("Pregunta:", obtener_pregunta())
    elif opcion == "3":
        print("¡Hasta luego! Sigue estudiando :)")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
