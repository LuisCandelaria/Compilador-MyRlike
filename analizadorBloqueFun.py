# -----------------------------------------------------------------------------
# analizadorBloqueFun.py
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

import analizadorArbol as aA
import analizadorExpresiones as aE
import analizadorCuadruplosExp as aCE
import sys

pila = []
tree = []
contador = 1

def an_label(hijo):
    global tree
    label = aA.gimmeTheLabel(tree, hijo)
    value  = aA.gimmeTheValue(label)
    return value

def an_identLonely(identLonely):
    global tree
    hijos = aA.gimmeTheChildren(identLonely, tree)
    ID = hijos[0]
    ID = an_label(ID)
    return [ID]

def an_identArray(identArray):
    global tree
    hijos = aA.gimmeTheChildren(identArray, tree)
    ID = hijos[0]
    ID = an_label(ID)
    expression = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    return [ID, '-[-'] + pilaExp + ['-]-']

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

def an_assignment(assignment):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(assignment, tree)
    identifier = hijos[0]
    expression = hijos[2]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    ID = an_identifier(identifier)
    stack = ID + ['='] + pilaExp
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += cuadruplos
    finalQuad = ['='] + ID + IDFinal
    pila += [finalQuad]

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
        pila += finalQuad

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
        pila += finalQuad
    if(value2 == "writingFinal"):
        writingFinal = hijo2
        an_writingFinal(writingFinal)
    elif(value2 == "writingRecursive"):
        writingRecursive = hijo2
        an_writingRecursive(writingRecursive)

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

def an_callRecursive(callRecursive):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(callRecursive, tree)
    expression = hijos[0]
    callAux = hijos[1]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    if(len(cuadruplos) != 1):
        pila += cuadruplos
    IDFinal = quads[1]
    contador = quads[2]
    finalStack = IDFinal
    return finalStack + an_callAux(callAux)

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
        if(len(cuadruplos) != 1):
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

def an_functionCall(functionCall):
    global tree
    global pila
    hijos = aA.gimmeTheChildren(functionCall, tree)
    ID = hijos[0]
    callAux = hijos[1]
    ID = an_label(ID)
    stack = an_callAux(callAux)
    finalQuad = ['callFunction', ID] + stack
    pila += [finalQuad]

def an_returnStatement(returnStatement):
    global tree
    global pila
    global contador
    hijos = aA.gimmeTheChildren(returnStatement, tree)
    expression = hijos[0]
    pilaExp = aE.init(expression, tree)
    aE.pila = []
    quads = aCE.init(pilaExp, contador)
    aCE.pila = []
    cuadruplos = quads[0]
    IDFinal = quads[1]
    contador = quads[2]
    pila += cuadruplos
    finalQuad = ['return'] + IDFinal
    pila += [finalQuad]

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

def error(hijo):
    print('Error')

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

def an_blockRecursive(blockRecursive):
    global tree
    hijos = aA.gimmeTheChildren(blockRecursive, tree)
    statute = hijos[0]
    blockAux = hijos[1]
    an_statute(statute)
    an_blockAux(blockAux)

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

def an_block(block):
    global tree
    hijos = aA.gimmeTheChildren(block, tree)
    blockAux = hijos[0]
    an_blockAux(blockAux)

def remakeStack(pila):
    contador = 1
    diccionario = {}
    pending = []
    jumps = []
    for index in range(len(pila)):
        quad = pila[index]
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

def init(block, lista):
    global tree
    global pila
    tree = lista
    an_block(block)
    diccionario = remakeStack(pila)
    pila = []
    return diccionario