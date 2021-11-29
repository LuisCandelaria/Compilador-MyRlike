# -----------------------------------------------------------------------------
# roma.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# El objetivo de este archivo es ser el intermediario con todos los analizadores
# que llenan los diccionarios, como el de variables globales, funciones, estatutos,
# etc. El nombre del archivo es inspirado por la frase: "Todos los caminos llegan
# a roma".
#
# Indice:
# 1. Archivos de que serán importados
# 2. Lista de diccionarios
# 3. Funcion inicial
# -----------------------------------------------------------------------------

from classVariables import *
import analizadorArbol as aA
import analizadorVarGlobales as aVG
import analizadorFunciones as aF
import analizadorBloqueFun as aBF
import millenium as millenium
import mountDoom as mD

dictVariablesGlobales = {}
dictFunciones = {}
dictEstatutos = {}
tree = []

# Función que analiza el valor de una etiqueta
def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

# Función que analiza la regla: principal
def an_principal(principal):
    global tree
    global dictEstatutos
    hijos = aA.gimmeTheChildren(principal, tree)
    block = hijos[0]
    dictEstatutos = aBF.init(block, tree)

# Función principal que reparte los caminos, ya sea si se necesita buscar variables globales, funciones, etc.
def principal():
    global tree
    hijos = aA.gimmeTheChildren("3", tree)
    label = aA.gimmeTheLabel(tree, '3')
    value = aA.gimmeTheValue(label)
    if(value == 'programVer1'):
        principal = hijos[2]
        an_principal(principal)
    elif(value == 'programVer2'):
        principal = hijos[1]
        an_principal(principal)
    else:
        principal = hijos[0]
        an_principal(principal)

# Función que inicia el análisis de funciones
def funciones():
    global tree
    global dictFunciones
    label = aA.gimmeTheLabel(tree, "3")
    value = aA.gimmeTheValue(label)
    if(value == "programVer1"):
        hijos = aA.gimmeTheChildren("3", tree)
        functions = hijos[1]
        dictFunciones = aF.init(functions, tree)
    elif(value == "programVer2"):
        hijos = hijos = aA.gimmeTheChildren("3", tree)
        hijo = hijos[0]
        label = aA.gimmeTheLabel(tree, hijo)
        value = aA.gimmeTheValue(label)
        if(value == "functions"):
            functions = hijo
            dictFunciones = aF.init(functions, tree)

# Función que inicia el análisis de variables globales
def variablesGlobales():
    global tree
    global dictVariablesGlobales
    label = aA.gimmeTheLabel(tree, "3")
    value = aA.gimmeTheValue(label)
    if(value == "programVer1"):
        hijos = aA.gimmeTheChildren("3", tree)
        vars = hijos[0]
        dictVariablesGlobales = aVG.init(vars, tree)
    elif(value == "programVer2"):
        hijos = hijos = aA.gimmeTheChildren("3", tree)
        hijo = hijos[0]
        label = aA.gimmeTheLabel(tree, hijo)
        value = aA.gimmeTheValue(label)
        if(value == "variables"):
            vars = hijo
            dictVariablesGlobales = aVG.init(vars, tree)

# Función inicial que recibe el árbol semántico y comienza la creación de todo el análisis
def init(lista):
    global tree
    global dictEstatutos
    global dictFunciones
    global dictVariablesGlobales
    tree = lista
    variablesGlobales()
    funciones()
    principal()
    #print(dictFunciones['fib'].estatutos)
    stack = millenium.init(dictVariablesGlobales, dictEstatutos, dictFunciones)
    #memoryMap = stack[1]
    #dictEstatutos = stack[0]