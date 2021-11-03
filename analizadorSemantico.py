# -----------------------------------------------------------------------------
# analizadorSemantico.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Nota y comentarios:
# El objetivo de este archivo es representar en forma de arbol todas las
# instrucciones del archivo de prueba, por ejemplo:
# principal tiene 3 hijos
#       hijo 1: variables globales
#       hijo 2: funciones
#       hijo 3: bloque
# Y de ahí, variables, funciones y bloques tendrán otros hijos, todo esto se
# puede entender viendo las reglas de sintaxis, y con el resultado de traducir
# cada clase, es decir, teniendo el arbol en forma de lista, se podrá analizar
# todo, y estos análisis se ejecutarán desde analizadorSintactico.py
#
# Indice:
# 1. Función de contador
# 2. Clase Node
# 3. Clases de la gramática
# -----------------------------------------------------------------------------

txt = " "
cont = 0

def incrementarContador():
    global cont
    cont += 1
    return "%d" %cont

class Node():
    pass

class Null(Node):
    def __init__(self):
        self.type = 'void'
    
    def imprimir(self, ident):
        print(ident + "nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + "nulo" + "]" + "\n"
        
        return id

class program(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return("digraph G {" + "\n" + txt + "}")

class programVer1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class programVer2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class programVer3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class variables(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class varAux(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class oneVar(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class sameType(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class sameTypeFinal(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class sameTypeRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class newType(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class functions(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class recursiveFunc(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class funcAux(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class typeFunction(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Tipo: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Tipo = "+str(self.name)+"]"+"\n"
        
        return id

class withParameters(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class funcVer1(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class funcVer2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class variablesLoc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class varAuxLoc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class oneVarLoc(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class sameTypeLoc(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class sameTypeFinalLoc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class sameTypeRecursiveLoc(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class newTypeLoc(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class parameters(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class oneParam(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class sameTypeParam(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class sameTypeParamFinal(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class sameTypeParamRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class newParam(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class identifierVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class identArrayVar(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class typeVar(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Tipo: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Tipo = "+str(self.name)+"]"+"\n"
        
        return id

class principal(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class block(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class blockAux(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class blockFinal(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Vacío: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Vacío = "+str(self.name)+"]"+"\n"
        
        return id

class blockRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class statute(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class assignment(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class returnStatement(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class ifStatement(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class shortCondition(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class longCondition(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class plotXYFunc(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class regressionFunc(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class writing(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class writingAux(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class writingFinal(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class writingString(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class writingRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class reading(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class readingAux(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class readingFinal(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class readingRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class loop(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class conditional(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class nonconditional(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" " + ident)
        else:
            self.son5.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        txt += id + "->" + son4 + "\n"
        txt += id + "->" + son5 + "\n"
        return id

class functionCall(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class callAux(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class callRecursive(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class callFinal(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Vacío: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Vacío = "+str(self.name)+"]"+"\n"
        
        return id

class expression(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class expressionOperation(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class term(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class termOperation(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class factor(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class factorOperation(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class idioms(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class idiomsOperation(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class auction(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class constant(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class someInt(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class someFloat(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class someChar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class otherExpression(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class identifier(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class identLonely(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class identArray(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id

class averageFunc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class modeFunc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class varianceFunc(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class expressionVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class expressionOperationVar(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class termVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class termOperationVar(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id

class auctionVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class constantVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class otherExpressionVar(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id

class ID(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"ID: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[ID = "+str(self.name)+"]"+"\n"
        
        return id

class String(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"String: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Sttring = "+str(self.name)+"]"+"\n"
        
        return id

class Operador(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Operador: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Operador = "+str(self.name)+"]"+"\n"
        
        return id

class OperadorLogico(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"OperadorLogico: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[OperadorLogico = "+str(self.name)+"]"+"\n"
        
        return id

class Int(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Entero: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Entero = "+str(self.name)+"]"+"\n"
        
        return id

class Float(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Flotante: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Flotante = "+str(self.name)+"]"+"\n"
        
        return id

class Char(Node):
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Char: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Char = "+str(self.name)+"]"+"\n"
        
        return id