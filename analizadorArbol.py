# -----------------------------------------------------------------------------
# analizadorArbol.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# El objetivo de este archivo es contener las funciones que ayudarán a todos
# los analizadores que impliquen el uso del arbol resultante del analizador
# semántico, con estas funciones se podrá seguir el camino de cada regla
# sintáctica quee usó el usuario.
#
# Indice:
# 1. Función que obtiene los hijos de un nodo
# 2. Función que obtiene la etiqueta del nodo
# 3. Función que obtiene el valor del nodo
# -----------------------------------------------------------------------------

def gimmeTheChildren(hijo, lista):
    lenght = len(lista)
    hijos = []
    tamañoHijo = len(hijo)
    substr = hijo + "-"
    for index in range(lenght):
        string = lista[index]
        sub = string.find(substr, 0, tamañoHijo+1)
        if(sub != -1):
            newstr = string[tamañoHijo+2:len(string)]
            hijos.append(newstr)
    return hijos

def gimmeTheLabel(lista, hijo):
    lenght = len(lista)
    tamañoHijo = len(hijo)
    substr = hijo + "["
    for index in range(lenght):
        string = lista[index]
        sub = string.find(substr, 0, tamañoHijo+1)
        if(sub != -1):
            newstr = string[tamañoHijo:len(string)]
            return newstr

def gimmeTheValue(label):
    index = label.find("=", 0, len(label))
    value = label[index+2:len(label)]
    value = value[:-1]
    return value