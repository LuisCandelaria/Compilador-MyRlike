# -----------------------------------------------------------------------------
# classMemory.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
#
# Indice:
#
# -----------------------------------------------------------------------------

import sys
from classVariables import *

class StackMemory():
    def __init__(self, tipo, tamaño, DirInicio, DirLimite):
        self.tipo = tipo
        self.tamaño = tamaño
        self.DirInicio = DirInicio
        self.Stack = ['#'] * self.tamaño
        self.contador = DirInicio
        self.DirLimite = DirLimite
    
    def assignSpace(self, obj):
        if(self.contador >= self.DirLimite):
            print("Stack overflow")
            sys.exit()
        if(obj.especie == 'Comun'):
            address = self.contador
            self.Stack[self.contador - self.DirInicio] = obj.valor
            self.contador += 1
            return self.contador
        else:
            size = obj.tamaño
            inicio = self.contador
            for i in range(0, size):
                if(self.contador >= self.DirLimite):
                    print("Stack overflow")
                    sys.exit()
                self.Stack[self.contador - self.DirInicio] = obj.valor[i]
                self.contador += 1
            return [inicio, self.contador]

    def assignRegularSpace(self):
        address = self.contador
        self.Stack[self.contador - self.DirInicio] = 0
        self.contador += 1
        return self.contador
    
    def getValue(self, address):
        if(address < self.DirInicio or address > self.DirLimite):
            print("Error en la dirección de memoria")
            sys.exit()
        return self.Stack[address - self.DirInicio]

    def setValue(self, address, valor):
        self.Stack[address - self.DirInicio] = valor