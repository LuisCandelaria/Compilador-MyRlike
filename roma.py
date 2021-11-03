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

dictVariablesGlobales = {}
dictFunciones = {}

def funciones(tree):
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

def variablesGlobales(tree):
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

def init(tree):
    variablesGlobales(tree)
    funciones(tree)