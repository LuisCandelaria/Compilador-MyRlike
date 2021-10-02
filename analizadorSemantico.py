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

class programVer1(Node):

class programVer2(Node):

class programVer3(Node):

class variables(Node):

class varAxu(Node):

class oneVar(Node):

class sameType(Node):

class sameTypeFinal(Node):

class sameTypeRecursive(Node):

class newType(Node):

class functions(Node):

class recursiveFunc(Node):

class funcAux(Node):

class typeFunction(Node):

class withParameters(Node):

class funcVer1(Node):

class funcVer2(Node):

class variablesLoc(Node):

class varAuxLoc(Node):

class oneVarLoc(Node):

class sameTypeLoc(Node):

class sameTypeFinalLoc(Node):

class sameTypeRecursiveLoc(Node):

class newTypeLoc(Node):

class parameters(Node):

class oneParam(Node):

class sameTypeParam(Node):

class sameTypeParamFinal(Node):

class sameTypeParamRecursive(Node):

class newParam(Node):

class identifierVar(Node):

class identLonelyVar(Node):

class identArrayVar(Node):

class type(Node):

class principal(Node):

class block(Node):

class blockAux(Node):

class blockFinal(Node):

class blockRecursive(Node):

class statute(Node):

class assignment(Node):

class returnStatement(Node):

class ifStatement(Node):

class shortCondition(Node):

class longCondition(Node):

class plotXYFunc(Node):

class regressionFunc(Node):

class writing(Node):

class writingAux(Node):

class writingFinal(Node):

class writingString(Node):

class writingRecursive(Node):

class reading(Node):

class readingAux(Node):

class readingFinal(Node):

class readingRecursive(Node):

class loop(Node):

class conditional(Node):

class nonconditional(Node):

class functionCall(Node):

class callAux(Node):

class callRecursive(Node):

class expression(Node):

class expressionOperation(Node):

class term(Node):

class termOperation(Node):

class factor(Node):

class factorOperation(Node):

class idioms(Node):

class idiomsOperation(Node):

class auction(Node):

class constant(Node):

class someInt(Node):

class someFloat(Node):

class someChar(Node):

class otherExpression(Node):

class identifier(Node):

class identLonely(Node):

class identArray(Node):

class averageFunc(Node):

class modeFunc(Node):

class varianceFunc(Node):

class expressionVar(Node):

class expressionOperationVar(Node):

class termVar(Node):

class termOperationVar(Node):

class auctionVar(Node):

class constantVar(Node):

class otherExpressionVar(Node):

class ID(Node):

class String(Node):

class Operador(Node):

class OperadorLogico(Node):

class Int(Node):

class Float(Node):

class Char(Node):