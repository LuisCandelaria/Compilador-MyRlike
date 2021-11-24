# -----------------------------------------------------------------------------
# classVariables.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# El objetivo de este archivo es gestionar las variables globales y locales
# de las funciones en un diccionario que contenga objetos, los objetos
# tendrán información importante de cada variable como: ID, valor, tipo y
# especie, este último siendo la etiqueta de si es una variable común o
# un arreglo. La clase también tendrá una función especial para asignar un valor,
# con esto cuando se tengan los cuádruplos, se podrá de manera automática asignar
# el valor a una variable teniendo el ID de otra o un temporal.
#
# Indice:
# 1. Clase variable común
# 2. Clase variable arreglo
# -----------------------------------------------------------------------------

class VariableComun():
    especie = "Comun"
    def __init__(self, ID, tipo):
        self.ID = ID
        self.tipo = tipo
        if(tipo == "int"):
            self.valor = 0
        elif(tipo == "float"):
            self.valor = 0.0
        elif(tipo == "char"):
            self.valor = '_'
    
    def imprimirDatos(self):
        print(self.ID + "\t" + self.tipo + "\t" + self.especie + "\t" + str(self.valor))
    
    def asignar(self, nuevo):
        self.valor = nuevo
    
    def getValue(self):
        return self.valor


class VariableArreglo():
    especie = "Arreglo"
    def __init__(self, ID, tamaño, tipo):
        self.ID = ID
        self.tamaño = int(tamaño)
        self.tipo = tipo
        if(tipo == "int"):
            self.valor = [0] * self.tamaño
        elif(tipo == "float"):
            self.valor = [0.0] * self.tamaño
        elif(tipo == "char"):
            self.valor = ['_'] * self.tamaño
    
    def imprimirDatos(self):
        print(self.ID + "\t" + str(self.tamaño) + "\t" + self.tipo + "\t" + self.especie + "\t" + str(self.valor))
    
    def asignar(self, nuevo, indice):
        self.valor[indice] = nuevo

    def getValue(self):
        return self.valor
    
    def getValueIndex(self, indice):
        return self.valor[indice]
    
    def asignarDireccion(self, direccion):
        self.address = direccion