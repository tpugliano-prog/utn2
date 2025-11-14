# diccionario.py
# Módulo encargado de almacenar definiciones básicas.

def obtener_definicion(termino):
    definiciones = {
        "fotosíntesis": "Proceso mediante el cual las plantas convierten la luz solar en energía química.",
        "mitosis": "Proceso de división celular que produce dos células hijas idénticas.",
        "ecosistema": "Conjunto de organismos que interactúan entre sí y con su ambiente.",
    }

    termino = termino.lower()
    return definiciones.get(termino, "Lo siento, no tengo la definición de ese término.")
