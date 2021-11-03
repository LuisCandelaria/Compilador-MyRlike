# -----------------------------------------------------------------------------
# classFunciones.py
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

class FuncionReturn():
    especie = "Retorno"
    def __init__(self, ID, tipo, parametros, variablesLocales, estatutos):
        self.ID = ID
        self.tipo = tipo
        self.parametros = parametros
        self.variablesLocales = variablesLocales
        self.estatutos = estatutos
    
    def imprimirDatos(self):
        print(self.ID + "\t" self.tipo + "\t")

class FunctionVoid():
    especie = "Void"
    def __init__(self, ID, parametros, variablesLocales, estatutos):
        self.ID = ID
        self.parametros = parametros
        self.variablesLocales = variablesLocales
        self.estatutos = estatutos
    
    def imprimirDatos(self):
        print(self.ID + "\t" self.especie + "\t")

