# -----------------------------------------------------------------------------
# analizadorBloqueFun.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo analiza el árbol semántico a partir del nodo bloque, el archivo
# al final regresará un diccionario de estatutos, sus puntos neurálgicos
# también son considerados en este análisis. Esta archivo es para cualquier
# bloque, ya sea el principal o el de una función.
#
# Indice:
# 1. Imports
# 2. Analizador del bloque y sus derivados
# 3. Recreación de los cuádruplos
# 4. Función inicial
# 
# -----------------------------------------------------------------------------

import analizadorArbol as aA
import analizadorExpresiones as aE
import analizadorCuadruplosExp as aCE
import sys

pila = []
tree = []
contador = 1

# Función que regresa el valor de una etiqueta
def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

# Función que analiza la regla identLonely
def an_identLonely(identLonely):
    global tree
    hijos = aA.gimmeTheChildren(identLonely, tree)
    ID = hijos[0]
    ID = an_label(ID)
    return [ID]

# Función que analiza la regla identArray
def an_identArray(identArray):
    global tree
    hijos = aA.gimmeTheChildren(identArray, tree)
    ID = hijos[0]
    ID = an_label(ID)
    expression = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    stack = [ID, '-[-'] + pilaExp + ['-]-']
    return stack

# Función que analiza la regla identifier
def an_identifier(identifier):
    global tree
    hijos = aA.gimmeTheChildren(identifier, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "identLonely"):
        identLonely = hijo
        ID = an_identLonely(identLonely)
        return ID
    else:
        identArray = hijo
        ID = an_identArray(identArray)
        return ID

# Función que analiza la regla assignment
def an_assignment(assignment):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(assignment, tree)
    identifier = hijos[0]
    expression = hijos[2]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    if(len(pilaExp) > 2):
        if(pilaExp[2] == []):
            del pilaExp[2]
    ID = an_identifier(identifier)
    stack = ID + ['='] + pilaExp
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplosID = []
    contador = quads[2]
    contador += 1
    if(len(ID) > 1):
        if(ID[1] == '-[-'):
            quadsID = aCE.init(ID, contador)
            aCE.pila = []
            cuadruplosID = quadsID[0][1]
            pila += [cuadruplosID]
            ID = quadsID[1]
            contador = quads[2]

    cuadruplos = quads[0]
    IDFinal = quads[1]
    quadsExp = []
    if(isinstance(IDFinal, list)):
        if(len(IDFinal) == 1):
            do = "nothinng"
        else:
            IDFinal = IDFinal[0][2]
            IDFinal = [IDFinal]
    contador = quads[2]
    pila += cuadruplos
    if(cuadruplosID != []):
        finalQuad = ['='] + ID + IDFinal
    else:
        finalQuad = ['='] + ID + IDFinal
    pila += [finalQuad]

# Función que analiza la regla shortCondition (if incompleto)
def an_shortCondition(shortCondition):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(shortCondition, tree)
    expression = hijos[0]
    block = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += cuadruplos
    finalQuad = ['GotoF'] + IDFinal
    pila += [finalQuad]
    an_block(block)
    pila += [['EndOfIf']]

# Función que analiza la regla longCondition (if completo)
def an_longCondition(longCondition):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(longCondition, tree)
    expression = hijos[0]
    block1 = hijos[1]
    block2 = hijos[2]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += cuadruplos
    finalQuad = ['GotoF'] + IDFinal
    pila += [finalQuad]
    an_block(block1)
    pila += [['GotoT']]
    pila += [['BeginElse']]
    an_block(block2)
    pila += [['EndOfIf']]

# Función que analiza el nodo padre: regla ifStatement
def an_ifStatement(ifStatement):
    global tree
    hijos = aA.gimmeTheChildren(ifStatement, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "shortCondition"):
        shortCondition = hijo
        an_shortCondition(shortCondition)
    else:
        longCondition = hijo
        an_longCondition(longCondition)
    
# Función que analiza la regla writingFinal
def an_writingFinal(writingFinal):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(writingFinal, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "writingString"):
        hijosDeString = aA.gimmeTheChildren(hijo, tree)
        hijoStr = hijosDeString[0]
        string = an_label(hijoStr)
        quad = ['writeStr', string]
        pila += [quad]
    else:
        expression = hijo
        pilaExp = aE.init(expression, tree)
        aE.pila = []
        quads = aCE.init(pilaExp, contador)
        aCE.pila = []
        cuadruplos = quads[0]
        IDFinal = quads[1]
        contador = quads[2]
        pila += cuadruplos
        finalQuad = ['writeExp'] + IDFinal
        pila += [finalQuad]

# Función que analiza la regla recursiva writingRecursive 
def an_writingRecursive(writingRecursive):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(writingRecursive, tree)
    hijo1 = hijos[0]
    hijo2 = hijos[1]
    value1 = an_label(hijo1)
    value2 = an_label(hijo2)
    if(value1 == "writingString"):
        hijosDeString = aA.gimmeTheChildren(hijo1, tree)
        hijoStr = hijosDeString[0]
        string = an_label(hijoStr)
        quad = ['writeStr', string]
        pila += [quad]
    elif(value1 == "expression"):
        expression = hijo1
        pilaExp = aE.init(expression, tree)
        aE.pila = []
        quads = aCE.init(pilaExp, contador)
        aCE.pila = []
        cuadruplos = quads[0]
        IDFinal = quads[1]
        contador = quads[2]
        pila += cuadruplos
        finalQuad = ['writeExp'] + IDFinal
        pila += [finalQuad]
    if(value2 == "writingFinal"):
        writingFinal = hijo2
        an_writingFinal(writingFinal)
    elif(value2 == "writingRecursive"):
        writingRecursive = hijo2
        an_writingRecursive(writingRecursive)

# Función que analiza el nodo padre de escritura: writing
def an_writing(writing):
    global tree
    hijos = aA.gimmeTheChildren(writing, tree)
    writingAux = hijos[0]
    hijos = aA.gimmeTheChildren(writingAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "writingFinal"):
        writingFinal = hijo
        an_writingFinal(writingFinal)
    else:
        writingRecursive = hijo
        an_writingRecursive(writingRecursive)

# Función que lee directamente los IDs en la regla identfier
def an_identifierRead(identifier):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(identifier, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "identLonely"):
        identLonely = hijo
        hijosLonely = aA.gimmeTheChildren(identLonely, tree)
        hijoLonely = hijosLonely[0]
        ID = an_label(hijoLonely)
        return ID
    else:
        identArray = hijo
        hijosArray = aA.gimmeTheChildren(identArray, tree)
        hijoID = hijosArray[0]
        expression = hijosArray[1]
        ID = an_label(hijoID)
        pilaExp = aE.init(expression, tree)
        aE.pila = []
        quads = aCE.init(pilaExp, contador)
        aCE.pila = []
        cuadruplos = quads[0]
        IDFinal = quads[1]
        contador = quads[2]
        pila += cuadruplos
        salida = ID + '[' + IDFinal[0] + ']' 
        return salida

# Función que analiza la regla recursiva readingRecursive
def an_readingRecursive(readingRecursive):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(readingRecursive, tree)
    identifier = hijos[0]
    hijo = hijos[1]
    ID = an_identifierRead(identifier)
    quad = ['read', ID]
    pila += [quad]
    value = an_label(hijo)
    if(value == "readingRecursive"):
        readingRecursive = hijo
        an_readingRecursive(readingRecursive)
    else:
        readingFinal = hijo
        hijosRF = aA.gimmeTheChildren(readingFinal, tree)
        identifier = hijosRF[0]
        ID = an_identifierRead(identifier)
        quad = ['read', ID]
        pila += [quad]

# Función que analiza el nodo padre de lectura: reading
def an_reading(reading):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(reading, tree)
    readingAux = hijos[0]
    hijos = aA.gimmeTheChildren(readingAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "readingFinal"):
        readingFinal = hijo
        hijosRF = aA.gimmeTheChildren(readingFinal, tree)
        identifier = hijosRF[0]
        ID = an_identifierRead(identifier)
        quad = ['read', ID]
        pila += [quad]
    else:
        readingRecursive = hijo
        an_readingRecursive(readingRecursive)

# Función que analiza la regla del ciclo For
def an_conditional(conditional):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(conditional, tree)
    expression = hijos[0]
    block = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += [['StartLoop']]
    pila += cuadruplos
    finalQuad = ['GotoF'] + IDFinal
    pila += [finalQuad]
    an_block(block)
    pila += [['GotoT']]
    pila += [['EndOfLoop']]

# Función que analiza la regla del ciclo While
def an_nonconditional(nonconditional):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(nonconditional, tree)
    assignment = hijos[0]
    expression = hijos[1]
    block = hijos[2]
    an_assignment(assignment)
    lastQuad = pila[-1]
    ID = lastQuad[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += [['StartLoop']]
    pila += cuadruplos
    finalQuad = ['GotoF'] + IDFinal
    pila += [finalQuad]
    an_block(block)
    temporal = 't' + str(contador)
    contador += 1
    nwQuad = ['+', ID, '1', temporal]
    nwAssign = ['=', ID, temporal]
    pila += [nwQuad]
    pila += [nwAssign]
    pila += [['GotoT']]
    pila += [['EndOfLoop']]

# Función que analiza el nodo padre de los ciclos: loop
def an_loop(loop):
    global tree
    hijos = aA.gimmeTheChildren(loop, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "conditional"):
        conditional = hijo
        an_conditional(conditional)
    else:
        nonconditional = hijo
        an_nonconditional(nonconditional)

# Función que analiza la llamada recursiva (más de un parámetro) 
def an_callRecursive(callRecursive):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(callRecursive, tree)
    expression = hijos[0]
    callAux = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp[0], contador)
    aCE.pila = []
    cuadruplos = quads[0]
    if(len(cuadruplos) != 1):
        pila += cuadruplos
    IDFinal = quads[1]
    contador = quads[2]
    finalStack = IDFinal
    return finalStack + an_callAux(callAux)

# Función que analiza la regla auxiliar de la llamada de una función
def an_callAux(callAux):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(callAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == 'expression'):
        expression = hijo
        pilaExp = aE.init(expression, tree)
        aE.pila = []
        quads = aCE.init(pilaExp, contador)
        aCE.pila = []
        cuadruplos = quads[0]
        if(len(cuadruplos[0]) != 1):
            pila += cuadruplos
        IDFinal = quads[1]
        contador = quads[2]
        finalStack = IDFinal
        return finalStack
    elif(value == 'callRecursive'):
        callRecursive = hijo
        IDs = an_callRecursive(callRecursive)
        finalStack = IDs
        return finalStack
    else:
        return []

# Función que analiza la regla de una llamada a una función
def an_functionCall(functionCall):
    global tree
    global pila
    global contador
    aE.tree = tree
    aE.an_functionCall(functionCall)
    unaPila = aE.pila
    aE.pila = []
    if(len(unaPila) > 2):
        if(unaPila[2] == []):
            del unaPila[2]
    quads = aCE.init(unaPila, contador)
    aCE.pila = []
    quads = quads[0]
    if(len(quads) == 1):
        sys.exit()
        quads[0][0] = 'callFunction'
        del quads[0][len(quads[0])-1]
    else:
        del quads[0]
        quads[len(quads)-1][0] = 'callFunction'
    #del quads[-1][-1]
    lastQuad = quads[-1]
    ID = lastQuad[1]
    era = ['era', ID]
    quads = [era] + quads
    pila += quads

# Función que analiza el estatuto de retorno
def an_returnStatement(returnStatement):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(returnStatement, tree)
    expression = hijos[0]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    if(len(pilaExp) == 1):
        temp = 't' + str(contador)
        quad = ['=', temp, pilaExp[0]]
        pila += [quad]
        IDFinal = [temp]
        finalQuad = ['return'] + IDFinal
        pila += [finalQuad]
    else:
        if(len(pilaExp[1]) > 2):
            aux = [pilaExp[0]] + [pilaExp[1]]
            pilaExp = pilaExp[2:len(pilaExp)]
            quads = aCE.init(aux, contador)
            aCE.pila = []
            cuadruplos = quads[0]
            IDFinal = quads[1]
            contador = quads[2]
            pila += cuadruplos
            pilaExp[0] = IDFinal + [pilaExp[0][1], pilaExp[0][0]]
            pilaExp = pilaExp[0]
            quad = aCE.quickGen(pilaExp)
            contador = aCE.contador
            aCE.pila = []
            cuadruplos = [quad]
            IDFinal = quads[2]
            pila += cuadruplos
            finalQuad = ['return'] + [IDFinal]
            pila += [finalQuad]
        else:
            if(pilaExp[1] == []):
                del pilaExp[1]
            quads = aCE.init(pilaExp, contador)
            aCE.pila = []
            cuadruplos = quads[0]
            IDFinal = quads[1]
            contador = quads[2]
            pila += cuadruplos
            finalQuad = ['return'] + IDFinal
            pila += [finalQuad]

# Función que analiza la regla de la regressionn
def an_regressionFunc(regressionFunc):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(regressionFunc, tree)
    ID1 = hijos[0]
    ID2 = hijos[1]
    ID1 = an_label(ID1)
    ID2 = an_label(ID2)
    stack = ['regression', ID1, ID2]
    pila += [stack]

# Función que analiza la regla que grafica dos arreglos
def an_plotXYFunc(plotXYFunc):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(plotXYFunc, tree)
    ID1 = hijos[0]
    ID2 = hijos[1]
    ID1 = an_label(ID1)
    ID2 = an_label(ID2)
    stack = ['plot', ID1, ID2]
    pila += [stack]

# Función auxiliar de error
def error(hijo):
    print('Error')

# Función que contiene el switch de tipo de estatuto
def an_statute(statute):
    global tree
    hijos = aA.gimmeTheChildren(statute, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    switch_statute = {
        'assignment' : an_assignment,
        'ifStatement' : an_ifStatement,
        'writing' : an_writing,
        'reading' : an_reading,
        'loop' : an_loop,
        'functionCall' : an_functionCall,
        'returnStatement' : an_returnStatement,
        'regressionFunc' : an_regressionFunc,
        'plotXYFunc' : an_plotXYFunc
    }
    switch_statute.get(value, error)(hijo)

# Función que analiza la regla del bloque recursivo (más de un estatuto)
def an_blockRecursive(blockRecursive):
    global tree
    hijos = aA.gimmeTheChildren(blockRecursive, tree)
    statute = hijos[0]
    blockAux = hijos[1]
    an_statute(statute)
    an_blockAux(blockAux)

# Función que analiza la regla auxiliar del bloque
def an_blockAux(blockAux):
    global tree
    hijos = aA.gimmeTheChildren(blockAux, tree)
    hijo = hijos[0]
    value = an_label(hijo)
    if(value == "statute"):
        statute = hijo
        an_statute(statute)
    elif(value == "blockRecursive"):
        blockRecursive = hijo
        an_blockRecursive(blockRecursive)

# Función que analiza la regla del bloque
def an_block(block):
    global tree
    hijos = aA.gimmeTheChildren(block, tree)
    blockAux = hijos[0]
    an_blockAux(blockAux)

# Función que reescribe los cuádruplos tomando en cuenta los puntos neurálgicos (parte del código intermedio)
def remakeStack(pila):
    contador = 1
    diccionario = {}
    pending = []
    jumps = []
    for index in range(len(pila)):
        quad = pila[index]
        if(len(quad) == 0):
            ignore = ''
        else:
            inst = quad[0]
            if(inst == 'GotoF'):
                pending = [contador] + pending
            if(inst == 'EndOfIf'):
                jumps = jumps + [contador + 1]
                pend = pending.pop()
                prevQuad = diccionario[pend]
                jumpTo = jumps.pop()
                prevQuad += [jumpTo]
                diccionario[pend] = prevQuad
            if(inst == 'BeginElse'):
                jumps = jumps + [contador + 1]
                pend = pending.pop()
                prevQuad = diccionario[pend]
                jumpTo = jumps.pop()
                prevQuad += [jumpTo]
                diccionario[pend] = prevQuad
            if(inst == 'GotoT'):
                pending = [contador] + pending
            if(inst == 'StartLoop'):
                jumps = jumps + [contador + 1]
            if(inst == 'EndOfLoop'):
                jumps = jumps + [contador + 1]
                pend = pending.pop()
                prevQuad = diccionario[pend]
                jumpTo = jumps.pop()
                prevQuad += [jumpTo]
                diccionario[pend] = prevQuad
                pend = pending.pop()
                prevQuad = diccionario[pend]
                jumpTo = jumps.pop()
                prevQuad += [jumpTo]
                diccionario[pend] = prevQuad
            diccionario[contador] = quad
            contador += 1
    return diccionario

# Función inicial del archivo, recibe el nodo del bloque y regresa una pila de cuádruplos
def init(block, lista):
    global tree
    global pila
    tree = lista
    an_block(block)
    diccionario = remakeStack(pila)
    pila = []
    return diccionario