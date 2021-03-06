# -----------------------------------------------------------------------------
# classFunciones.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo contiene las clases para cada tipo de función
#
# Indice:
# 1. Import
# 2. Función de retorno
# 3. Función void
#
# -----------------------------------------------------------------------------

from classVariables import *

class FuncionReturn():
    especie = "Retorno"
    def __init__(self, ID, tipo, parametros, variablesLocales, estatutos):
        self.ID = ID
        self.tipo = tipo
        self.parametros = parametros
        self.variablesLocales = variablesLocales
        self.estatutos = estatutos
    
    def imprimirDatos(self):
        print(self.ID + "\t" + self.tipo + "\t" + self.especie)
        print(self.parametros)
        print(self.variablesLocales)
        print(self.estatutos)
    
    def setAddress(self, address):
        self.address = address

class FunctionVoid():
    especie = "Void"
    def __init__(self, ID, parametros, variablesLocales, estatutos):
        self.ID = ID
        self.parametros = parametros
        self.variablesLocales = variablesLocales
        self.estatutos = estatutos
    
    def imprimirDatos(self):
        print(self.ID + "\t" + self.especie + "\t")
        print(self.parametros)
        print(self.variablesLocales)
        print(self.estatutos)
    
    def setAddress(self, address):
        self.address = address