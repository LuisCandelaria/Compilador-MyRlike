# -----------------------------------------------------------------------------
# analizadorSintactico.py
# Version 1.1
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Nota y comentarios:
# El objetivo de este archivo es representar todas las reglas de sintaxis del
# compilador, para ver de manera eficiente las reglas dirigirse al archivo:
# 'Documentación.docx' en la sección de 'Gramática'. El archivo también
# funcionará como punto de partida para todos los análisis que se harán en
# en compilador, por ejemplo: analizadorVariablesGlobales,
# analizadorFunciones, etc. es como si el proyecto fuera un pulpo y este
# archivo fuera la cabeza del mismo y los demás archivos sus tentáculos.
#
# Indice:
# 1. Librerias
# 2. Precedencia
# 3. Gramática
# 4. Función de búsqueda de archivos de prueba
# 5. Función que traduce el archivo de prueba a formato de gráfica
# 6. Directorio
# 7. Parser
# 8. Renglones del arbol
# -----------------------------------------------------------------------------

# Librerías necesarias para la ejecución del archivo
import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from analizadorLexico import f_analisisLexico
from sys import stdin
from analizadorSemantico import *
import roma as rm

# Precedencia
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LTHAN', 'GTHAN', 'DIFF', 'EQUAL'),
    ('left', 'COLON', 'SEMICOLON', 'COMA'),
    ('left', 'LBRACK', 'RBRACK', 'LSBRACK', 'RSBRACK'),
    ('left', 'LPAREN', 'RPAREN')
)

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON programVer1
    | PROGRAM ID SEMICOLON programVer2
    | PROGRAM ID SEMICOLON programVer3
    '''
    p[0] = program(ID(p[2]), p[4], "program")

def p_programVer1(p):
    '''
    programVer1 : variables functions principal
    '''
    p[0] = programVer1(p[1], p[2], p[3], "programVer1")

def p_programVer2(p):
    '''
    programVer2 : variables principal
    | functions principal
    '''
    p[0] = programVer2(p[1], p[2], "programVer2")

def p_programVer3(p):
    '''
    programVer3 : principal
    '''
    p[0] = programVer3(p[1], "programVer3")

def p_variables(p):
    '''
    variables : VARS varAux
    '''
    p[0] = variables(p[2], "variables")

def p_varAux(p):
    '''
    varAux : oneVar
    | sameType
    | newType
    '''
    p[0] = varAux(p[1], "varAux")

def p_oneVar(p):
    '''
    oneVar : typeVar COLON identifierVar SEMICOLON
    '''
    p[0] = oneVar(p[1], p[3], "oneVar")

def p_sameType(p):
    '''
    sameType : typeVar COLON identifierVar COMA sameTypeFinal
    | typeVar COLON identifierVar COMA sameTypeRecursive
    '''
    p[0] = sameType(p[1], p[3], p[5], "sameType")

def p_sameTypeFinal(p):
    '''
    sameTypeFinal : identifierVar SEMICOLON
    '''
    p[0] = sameTypeFinal(p[1], "sameTypeFinal")

def p_sameTypeRecursive(p):
    '''
    sameTypeRecursive : identifierVar COMA sameTypeRecursive
    | identifierVar COMA sameTypeFinal
    | identifierVar SEMICOLON varAux
    '''
    p[0] = sameTypeRecursive(p[1], p[3], "sameTypeRecursive")

def p_newType(p):
    '''
    newType : typeVar COLON identifierVar SEMICOLON varAux
    '''
    p[0] = newType(p[1], p[3], p[5], "newType")

def p_functions(p):
    '''
    functions : funcAux
    | recursiveFunc
    '''
    p[0] = functions(p[1], "functions")

def p_recursiveFunc(p):
    '''
    recursiveFunc : funcAux functions
    '''
    p[0] = recursiveFunc(p[1], p[2], "recursiveFunc")

def p_funcAux(p):
    '''
    funcAux : FUNCTION typeFunction ID LPAREN withParameters
    | FUNCTION typeFunction ID LPAREN RPAREN funcVer1
    | FUNCTION typeFunction ID LPAREN RPAREN funcVer2
    '''
    p[0] = funcAux(p[2], ID(p[3]), p[5], "funcAux")

def p_typeFunction(p):
    '''
    typeFunction : INT
    | FLOAT
    | CHAR
    | VOID
    '''
    p[0] = typeFunction(p[1])

def p_withParameters(p):
    '''
    withParameters : parameters RPAREN funcVer1
    | parameters RPAREN funcVer2
    '''
    p[0] = withParameters(p[1], p[3], "withParameters")

def p_funcVer1(p):
    '''
    funcVer1 : variablesLoc block
    '''
    p[0] = funcVer1(p[1], p[2], "funcVer1")

def p_funcVer2(p):
    '''
    funcVer2 : block
    '''
    p[0] = funcVer2(p[1], "funcVer2")

def p_variablesLoc(p):
    '''
    variablesLoc : VARS varAuxLoc
    '''
    p[0] = variablesLoc(p[2], "variablesLoc")

def p_varAuxLoc(p):
    '''
    varAuxLoc : oneVarLoc
    | sameTypeLoc
    | newTypeLoc
    '''
    p[0] = varAuxLoc(p[1], "varAuxLoc")

def p_oneVarLoc(p):
    '''
    oneVarLoc : typeVar COLON identifier SEMICOLON
    '''
    p[0] = oneVarLoc(p[1], p[3], "oneVarLoc")

def p_sameTypeLoc(p):
    '''
    sameTypeLoc : typeVar COLON identifier COMA sameTypeFinalLoc
    | typeVar COLON identifier COMA sameTypeRecursiveLoc
    '''
    p[0] = sameTypeLoc(p[1], p[3], p[5], "sameTypeLoc")

def p_sameTypeFinalLoc(p):
    '''
    sameTypeFinalLoc : identifier SEMICOLON
    '''
    p[0] = sameTypeFinalLoc(p[1], "sameTypeFinalLoc")

def p_sameTypeRecursiveLoc(p):
    '''
    sameTypeRecursiveLoc : identifier COMA sameTypeRecursiveLoc
    | identifier COMA sameTypeFinalLoc
    | identifier SEMICOLON varAuxLoc
    '''
    p[0] = sameTypeRecursiveLoc(p[1], p[3], "sameTypeRecursiveLoc")

def p_newTypeLoc(p):
    '''
    newTypeLoc : typeVar COLON identifier SEMICOLON varAuxLoc
    '''
    p[0] = newTypeLoc(p[1], p[3], p[5], "newTypeLoc")

def p_parameters(p):
    '''
    parameters : oneParam
    | sameTypeParam
    | newParam
    '''
    p[0] = parameters(p[1], "parameters")

def p_oneParam(p):
    '''
    oneParam : typeVar COLON identifierVar
    '''
    p[0] = oneParam(p[1], p[3], "oneParam")

def p_sameTypeParam(p):
    '''
    sameTypeParam : typeVar COLON identifierVar COMA sameTypeParamFinal
    | typeVar COLON identifierVar COMA sameTypeParamRecursive
    '''
    p[0] = sameTypeParam(p[1], p[3], p[5], "sameTypeParam")

def p_sameTypeParamFinal(p):
    '''
    sameTypeParamFinal : identifierVar
    '''
    p[0] = sameTypeParamFinal(p[1], "sameTypeParamFinal")

def p_sameTypeParamRecursive(p):
    '''
    sameTypeParamRecursive : identifierVar  COMA sameTypeParamRecursive
    | identifierVar COMA sameTypeFinal
    | identifier SEMICOLON parameters
    '''
    p[0] = sameTypeParamRecursive(p[1], p[3], "sameTypeParamRecursive")

def p_newParam(p):
    '''
    newParam : typeVar COLON identifierVar SEMICOLON parameters
    '''
    p[0] = newParam(p[1], p[3], p[5], "newParam")

def p_identifierVar(p):
    '''
    identifierVar : identLonely
    | identArrayVar
    '''
    p[0] = identifierVar(p[1], "identifierVar")

def p_identArrayVar(p):
    '''
    identArrayVar : ID LSBRACK expressionVar RSBRACK
    '''
    p[0] = identArrayVar(ID(p[1]), p[3], "identArrayVar")

def p_typeVar(p):
    '''
    typeVar : INT
    | FLOAT
    | CHAR
    '''
    p[0] = typeVar(p[1])

def p_principal(p):
    '''
    principal : MAIN LPAREN RPAREN block
    '''
    p[0] = principal(p[4], "principal")

def p_block(p):
    '''
    block : LBRACK blockAux
    '''
    p[0] = block(p[2], "block")

def p_blockAux(p):
    '''
    blockAux : statute RBRACK
    | blockRecursive
    | blockFinal
    '''
    p[0] = blockAux(p[1], "blockAux")

def p_blockFinal(p):
    '''
    blockFinal : RBRACK
    '''
    p[0] = blockFinal("blockFinal")

def p_blockRecursive(p):
    '''
    blockRecursive : statute blockAux
    '''
    p[0] = blockRecursive(p[1], p[2], "blockRecursive")

def p_statute(p):
    '''
    statute : assignment SEMICOLON
    | ifStatement
    | writing SEMICOLON
    | reading SEMICOLON
    | loop
    | functionCall SEMICOLON
    | returnStatement SEMICOLON
    | regressionFunc SEMICOLON
    | plotXYFunc SEMICOLON
    '''
    p[0] = statute(p[1], "statute")

def p_assignment(p):
    '''
    assignment : identifier ASSIGN expression
    '''
    p[0] = assignment(p[1], Operador(p[2]), p[3], "assignment")

def p_returnStatement(p):
    '''
    returnStatement : RETURN LPAREN expression RPAREN
    '''
    p[0] = returnStatement(p[3], "returnStatement")

def p_ifStatement(p):
    '''
    ifStatement : shortCondition
    | longCondition
    '''
    p[0] = ifStatement(p[1], "ifStatement")

def p_shortCondition(p):
    '''
    shortCondition : IF LPAREN expression RPAREN THEN block
    '''
    p[0] = shortCondition(p[3], p[6], "shortCondition")

def p_longCondition(p):
    '''
    longCondition : IF LPAREN expression RPAREN THEN block ELSE block
    '''
    p[0] = longCondition(p[3], p[6], p[8], "longCondition")

def p_plotXYFunc(p):
    '''
    plotXYFunc : PLOTXY LPAREN ID COMA ID RPAREN
    '''
    p[0] = plotXYFunc(ID(p[3]), ID(p[5]), "plotXYFunc")

def p_regressionFunc(p):
    '''
    regressionFunc : REGRESSION LPAREN ID COMA ID RPAREN
    '''
    p[0] = regressionFunc(ID(p[3]), ID(p[5]), "regressionFunc")

def p_writing(p):
    '''
    writing : WRITE LPAREN writingAux
    '''
    p[0] = writing(p[3], "writing")

def p_writingAux(p):
    '''
    writingAux : writingFinal
    | writingRecursive
    '''
    p[0] = writingAux(p[1], "writingAux")

def p_writingFinal(p):
    '''
    writingFinal : writingString RPAREN
    | expression RPAREN
    '''
    p[0] = writingFinal(p[1], "writingFinal")

def p_writingString(p):
    '''
    writingString : CTE_STRING
    '''
    p[0] = writingString(String(p[1]), "writingString")

def p_writingRecursive(p):
    '''
    writingRecursive : writingString COMA writingFinal
    | expression COMA writingFinal
    | writingString COMA writingRecursive
    | expression COMA writingRecursive
    '''
    p[0] = writingRecursive(p[1], p[3], "writingRecursive")

def p_reading(p):
    '''
    reading : READ LPAREN readingAux
    '''
    p[0] = reading(p[3], "reading")

def p_readingAux(p):
    '''
    readingAux : readingFinal
    | readingRecursive
    '''
    p[0] = readingAux(p[1], "readingAux")

def p_readingFinal(p):
    '''
    readingFinal : identifier RPAREN
    '''
    p[0] = readingFinal(p[1], "readingFinal")

def p_readingRecursive(p):
    '''
    readingRecursive : identifier COMA readingRecursive
    | identifier COMA readingFinal
    '''
    p[0] = readingRecursive(p[1], p[3], "readingRecursive")

def p_loop(p):
    '''
    loop : conditional
    | nonconditional
    '''
    p[0] = loop(p[1], "loop")

def p_conditional(p):
    '''
    conditional : WHILE LPAREN expression RPAREN block
    '''
    p[0] = conditional(p[3], p[5], "conditional")

def p_nonconditional(p):
    '''
    nonconditional : FOR identifier ASSIGN expression TO expression DO block
    '''
    p[0] = nonconditional(p[2], Operador(p[3]), p[4], p[6], p[8], "nonconditional")

def p_functionCall(p):
    '''
    functionCall : ID LPAREN callAux
    '''
    p[0] = functionCall(ID(p[1]), p[3], "functionCall")

def p_callAux(p):
    '''
    callAux : expression RPAREN
    | callRecursive
    | callFinal
    '''
    p[0] = callAux(p[1], "callAux")

def p_callRecursive(p):
    '''
    callRecursive : expression COMA callAux
    '''
    p[0] = callRecursive(p[1], p[3], "callRecursive")

def p_callFinal(p):
    '''
    callFinal : RPAREN
    '''
    p[0] = callFinal("callFinal")

def p_expression(p):
    '''
    expression : term
    | expressionOperation
    '''
    p[0] = expression(p[1], "expression")

def p_expressionOperation(p):
    '''
    expressionOperation : term PLUS expression
    | term MINUS expression
    '''
    p[0] = expressionOperation(p[1], Operador(p[2]), p[3], "expressionOperation")

def p_term(p):
    '''
    term : factor
    | termOperation
    '''
    p[0] = term(p[1], "term")

def p_termOperation(p):
    '''
    termOperation : factor TIMES term
    | factor DIVIDE term
    '''
    p[0] = termOperation(p[1], Operador(p[2]), p[3], "termOperation")

def p_factor(p):
    '''
    factor : idioms
    | factorOperation
    '''
    p[0] = factor(p[1], "factor")

def p_factorOperation(p):
    '''
    factorOperation : idioms GTHAN factor
    | idioms LTHAN factor
    | idioms EQUAL factor
    | idioms DIFF factor
    '''
    p[0] = factorOperation(p[1], Operador(p[2]), p[3], "factorOperation")

def p_idioms(p):
    '''
    idioms : auction
    | idiomsOperation
    '''
    p[0] = idioms(p[1], "idioms")

def p_idiomsOperation(p):
    '''
    idiomsOperation : auction OR idioms
    | auction AND idioms
    '''
    p[0] = idiomsOperation(p[1], OperadorLogico(p[2]), p[3], "idiomsOperation")

def p_auction(p):
    '''
    auction : constant
    | otherExpression
    | identifier
    | averageFunc
    | modeFunc
    | varianceFunc
    | functionCall
    '''
    p[0] = auction(p[1], "auction")

def p_constant(p):
    '''
    constant : someInt
    | someFloat
    | someChar
    '''
    p[0] = constant(p[1], "constant")

def p_someInt(p):
    '''
    someInt : CTE_INT
    '''
    p[0] = someInt(Int(p[1]), "someInt")

def p_someFloat(p):
    '''
    someFloat : CTE_FLOAT 
    '''
    p[0] = someFloat(Float(p[1]), "someFloat")

def p_someChar(p):
    '''
    someChar : CTE_CHAR
    '''
    p[0] = someChar(Char(p[1]), "someChar")

def p_otherExpression(p):
    '''
    otherExpression : LPAREN expression RPAREN
    '''
    p[0] = otherExpression(p[2], "otherExpression")

def p_identifier(p):
    '''
    identifier : identLonely
    | identArray
    '''
    p[0] = identifier(p[1], "identifier")

def p_identLonely(p):
    '''
    identLonely : ID
    '''
    p[0] = identLonely(ID(p[1]), "identLonely")

def p_identArray(p):
    '''
    identArray : ID LSBRACK expression RSBRACK
    '''
    p[0] = identArray(ID(p[1]), p[3], "identArray")

def p_averageFunc(p):
    '''
    averageFunc : AVERAGE LPAREN ID RPAREN
    '''
    p[0] = averageFunc(ID(p[3]), "averageFunc")

def p_modeFunc(p):
    '''
    modeFunc : MODE LPAREN ID RPAREN
    '''
    p[0] = modeFunc(ID(p[3]), "modeFunc")

def p_varianceFunc(p):
    '''
    varianceFunc : VARIANCE LPAREN ID RPAREN
    '''
    p[0] = varianceFunc(ID(p[3]), "varianceFunc")

def p_expressionVar(p):
    '''
    expressionVar : termVar
    | expressionOperationVar
    '''
    p[0] = expressionVar(p[1], "expressionVar")

def p_expressionOperationVar(p):
    '''
    expressionOperationVar : termVar PLUS expressionVar
    | termVar MINUS expressionVar
    '''
    p[0] = expressionOperationVar(p[1], Operador(p[2]), p[3], "expressionOperationVar")

def p_termVar(p):
    '''
    termVar : auctionVar
    | termOperationVar
    '''
    p[0] = termVar(p[1], "termVar")

def p_termOperationVar(p):
    '''
    termOperationVar : auctionVar TIMES termVar
    | auctionVar DIVIDE termVar
    '''
    p[0] = termOperationVar(p[1], Operador(p[2]), p[3], "termOperationVar")

def p_auctionVar(p):
    '''
    auctionVar : constantVar
    | otherExpressionVar
    '''
    p[0] = auctionVar(p[1], "auctionVar")

def p_constantVar(p):
    '''
    constantVar : CTE_INT
    '''
    p[0] = constantVar(Int(p[1]), "constantVar")

def p_otherExpressionVar(p):
    '''
    otherExpressionVar : LPAREN expressionVar RPAREN
    '''
    p[0] = otherExpressionVar(p[2], "otherExpressionVar")

def p_error(p):
    print("Error de sintaxis")
    print("Error en la línea " + str(p.lineno))

# ............................................................... #
# Función que sirve para traer todo los archivos de la carpeta
# Test, para elejir un archivo de prueba y así ejecutar los
# analizadores (léxico, semántico, etc.)
# ............................................................... #
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    
    for file in files:
        print(str(cont) + ". " + file)
        cont += 1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    
    print("Has escogido \%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]

# ............................................................... #
# Esta función traduce todas las instrucciones que se escribieron
# en el archivo de prueba a un formato de gráfica, el archivo
# resultante tendrá una serie de lineas que señalan qué
# instrucción de escribió y las que le siguen, por ejemplo:
# si se llegó a la regla 'identifier', en la gráfica podemos ver
# cuál regla derivada se aplicó, ya sea identLonely o identArray.
# Este proceso le da un orden más estricto al compilador, aunque
# también hace al código más complejo.
# ............................................................... #
def traducir(result):
    graphFile = open('graph.txt', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print("El programa traducido se guardo en \"graph.txt\"")

# Dirección de la carpeta con los archivos de prueba, se debe cambiar si se está en otro dispositivo
directorio = '/Users/luiskande/Documents/Documentos ITESM/15º Semestre/Compiladores/Proyecto Final/Test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo

# Ejecución del analizadorLexico
f_analisisLexico(test)

# Lectura del archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

# Ejecución del parser
parser = yacc.yacc()
result = parser.parse(cadena)

# Ejecución de la traducción (analizadorSemantico)
traducir(result)

# ............................................................... #
# Esta función guarda todas las lineas del arbol en graph.txt en
# un arreglo para futuros analisis, también eliminar el espacio
# extra que se escribe en el 2do renglon del arbol, cosa que no he
# podido evitar.
# ............................................................... #
def clean():
    f = open("graph.txt", "r")
    text = f.read()
    f.close()
    lines = text.splitlines()
    lines.pop(0)
    lines.pop(len(lines)-1)
    line = lines[0]
    fixed = ""
    for i in range(1, len(line)):
        character = line[i]
        fixed += character
    lines[0] = fixed
    return lines

tree = clean()

rm.init(tree)