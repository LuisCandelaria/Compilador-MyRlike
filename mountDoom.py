# -----------------------------------------------------------------------------
# mountDoom.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Notas y comentarios:
# Este archivo resuelve lo que tiene un cuádruplo, regresa el mapa de memoria
# virtual con los valores o el índice cambiados
#
# Indice:
# 1. Imports
# 2. Variables globales
# 3. Función auxiliar
# 4. Versiones de solución
# 5. Función inicial
#
# -----------------------------------------------------------------------------

import sys
import numpy as np
from statistics import mode, multimode
import matplotlib.pyplot as plt
from classMemory import *

memoryMap = {}

inicioInt = 8000
inicioTempInt = 1000
inicioFloat = 9000
inicioTempFloat = 2000
inicioChar = 10000
inicioTempChar = 3000
inicioTempBool = 4000

waitingForReturn = []

# Función que regresa que tipo de Stack debe buscarse (de acuerdo a la dirección)
def verifyAddress(address):
    global inicioInt
    global inicioTempInt
    global inicioFloat
    global inicioTempFloat
    global inicioChar
    global inicioTempChar
    global inicioTempBool

    if(address >= inicioInt and address < inicioFloat):
        return 'globalInt'
    elif(address >= inicioFloat and address < inicioChar):
        return 'globalFloat'
    elif(address >= inicioChar):
        return 'globalChar'
    elif(address >= inicioTempInt and address < inicioTempFloat):
        return 'tempInt'
    elif(address >= inicioTempFloat and address < inicioTempChar):
        return 'tempFloat'
    elif(address >= inicioTempChar and address < inicioTempBool):
        return 'tempFloat'
    else:
        return 'tempBool'

# Solución al retorno
def an_return(quad, i):
    global memoryMap
    global waitingForReturn
    if(waitingForReturn == []):
        return i
    first = quad[1]
    addressFirst = ''
    lastCharacter = first[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        if(first.find('[') == -1):
            addressFirst = int(first)
        else:
            leftsqbrack = first.find('[')
            substr = first[0:leftsqbrack]
            dash = substr.find('-')
            firstAdd = substr[0:dash]
            firstAdd = int(firstAdd)
            secondAdd = substr[dash+1:len(substr)]
            secondAdd = int(secondAdd)
            indexAdd = first[leftsqbrack+1:len(first)-1]
            size = int(secondAdd) - int(firstAdd)
            indexAdd = int(indexAdd)
            keyIndex = verifyAddress(indexAdd)
            valueIndex = memoryMap[keyIndex].getValue(indexAdd)
            if(valueIndex < size or valueIndez >= size):
                print("Index out of range")
                sys.exit()
            else:
                firstAdd += valueIndex
                addressFirst = firstAdd
    
    keyStackFirst = verifyAddress(addressFirst)
    value = memoryMap[keyStackFirst].getValue(addressFirst)
    
    try:
        temp = waitingForReturn.pop()
        keyStackTemp = verifyAddress(temp)
        memoryMap[keyStackFirst].setValue(temp, value)
    except:
        do = "nothing"

    return i

# Solución al esperar un retorno, este agrega a una pila de espera al temporal que requiere un return
def an_retrieve(quad, i):
    global memoryMap
    global waitingForReturn
    first = quad[2]
    addressFirst = ''
    lastCharacter = first[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        if(first.find('[') == -1):
            addressFirst = int(first)
        else:
            leftsqbrack = first.find('[')
            substr = first[0:leftsqbrack]
            dash = substr.find('-')
            firstAdd = substr[0:dash]
            firstAdd = int(firstAdd)
            secondAdd = substr[dash+1:len(substr)]
            secondAdd = int(secondAdd)
            indexAdd = first[leftsqbrack+1:len(first)-1]
            size = int(secondAdd) - int(firstAdd)
            indexAdd = int(indexAdd)
            keyIndex = verifyAddress(indexAdd)
            valueIndex = memoryMap[keyIndex].getValue(indexAdd)
            if(valueIndex < size or valueIndez >= size):
                print("Index out of range")
                sys.exit()
            else:
                firstAdd += valueIndex
                addressFirst = firstAdd
    
    waitingForReturn += [addressFirst]

    return i

# Solución a la regresión
def an_regression(quad, i):
    global memoryMap
    first = quad[1]
    second = quad[2]
    addressFirst = ''
    addressSecond = ''

    lastCharacter = first[-1]
    stack1 = []
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        dash = first.find('-')
        firstAdd = first[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = first[dash+1:len(first)]
        secondAdd = int(secondAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack1 += [value]
    
    lastCharacter = first[-1]
    stack2 = []
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        dash = second.find('-')
        firstAdd = second[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = second[dash+1:len(second)]
        secondAdd = int(secondAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack1 += [value]
    
    x = np.array(stack1)
    y = np.array(stack2)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b)
    plt.show()
    return i+1

# Solución al gráfico de dos arreglos
def an_plot(quad, i):
    global memoryMap
    first = quad[1]
    second = quad[2]
    addressFirst = ''
    addressSecond = ''

    lastCharacter = first[-1]
    stack1 = []
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        dash = first.find('-')
        firstAdd = first[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = first[dash+1:len(first)]
        secondAdd = int(secondAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack1 += [value]
    
    lastCharacter = first[-1]
    stack2 = []
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        dash = second.find('-')
        firstAdd = second[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = second[dash+1:len(second)]
        secondAdd = int(secondAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack1 += [value]
    
    plt.plot(stack1, stack2)
    plt.show()
    return i

# Regresa la moda de una lista
def calculateMode(stack):
    mode = mode(stack)
    return mode

# Solución a la moda
def an_mode(quad, i):
    global memoryMap
    first = quad[1]
    addressFirst = ''
    second = quad[2]
    addressSecond = ''

    lastCharacter = first[-1]
    stack = []
    size = 0
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        dash = first.find('-')
        firstAdd = first[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = first[dash+1:len(first)]
        secondAdd = int(secondAdd)
        size = int(secondAdd) - int(firstAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack += [value]
    mode = calculateMode(stack)
    
    lastCharacter = second[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        addressSecond = int(second)
    keyStackSecond = verifyAddress(addressSecond)
    memoryMap[keyStackSecond].setValue(addressSecond, mode)
    return i

# Regresa la varianza de una lista
def calculateVariance(stack):
    variance = np.var(stack)
    return variance

# Solución a la varianza
def an_variance(quad, i):
    global memoryMap
    first = quad[1]
    addressFirst = ''
    second = quad[2]
    addressSecond = ''

    lastCharacter = first[-1]
    stack = []
    size = 0
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        dash = first.find('-')
        firstAdd = first[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = first[dash+1:len(first)]
        secondAdd = int(secondAdd)
        size = int(secondAdd) - int(firstAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack += [value]
    variance = calculateVariance(stack)
    
    lastCharacter = second[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        addressSecond = int(second)
    keyStackSecond = verifyAddress(addressSecond)
    memoryMap[keyStackSecond].setValue(addressSecond, variance)
    return i

# Regresa el promedio de una lista
def calculateAvg(stack, size):
    acum = 0
    for h in range(0, size):
        index = stack[h]
        acum += index
    avg = acum / size
    return avg

# Solución al promedio
def an_average(quad, i):
    global memoryMap
    first = quad[1]
    addressFirst = ''
    second = quad[2]
    addressSecond = ''

    lastCharacter = first[-1]
    stack = []
    size = 0
    average = 0
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        dash = first.find('-')
        firstAdd = first[0:dash]
        firstAdd = int(firstAdd)
        secondAdd = first[dash+1:len(first)]
        secondAdd = int(secondAdd)
        size = int(secondAdd) - int(firstAdd)
        keyStackFirst = verifyAddress(firstAdd)
        for j in range(firstAdd, secondAdd):
            value = memoryMap[keyStackFirst].getValue(j)
            stack += [value]
    average = calculateAvg(stack, size)
    
    lastCharacter = second[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        addressSecond = int(second)
    keyStackSecond = verifyAddress(addressSecond)
    memoryMap[keyStackSecond].setValue(addressSecond, average)
    return i

# Solución a la lectura
def an_read(quad, i):
    global memoryMap
    first = quad[1]
    addressFirst = ''

    lastCharacter = first[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        first = first[0:len(first)-1]
        if(first.find('[') == -1):
            addressFirst = int(first)
        else:
            leftsqbrack = first.find('[')
            substr = first[0:leftsqbrack]
            dash = substr.find('-')
            firstAdd = substr[0:dash]
            secondAdd = substr[dash+1:len(substr)]
            firstAdd = int(firstAdd)
            secondAdd = int(secondAdd)
            indexAdd = first[leftsqbrack+1:len(first)-1]
            size = int(secondAdd) - int(firstAdd)
            indexAdd = int(indexAdd)
            keyIndex = verifyAddress(indexAdd)
            valueIndex = memoryMap[keyIndex].getValue(indexAdd)
            if(valueIndex < 0 or valueIndex >= size):
                print("Index out of range")
                sys.exit()
            else:
                firstAdd += valueIndex
                addressFirst = firstAdd

    valueFirst = ''
    keyStackFirst = ''
    if(addressFirst != ''):
        keyStackFirst = verifyAddress(addressFirst)
        print("Ingresa valor: ")
        valueFirst = input()
        if(keyStackFirst == 'globalInt'):
            valueFirst = int(valueFirst)
        elif(keyStackFirst == 'globalFloat'):
            valueFirst = float(valueFirst)
        memoryMap[keyStackFirst].setValue(addressFirst, valueFirst)
    else:
        sys.exit()
    
    return i

# Solución a la escritura de un string
def an_writeStr(quad, i):
    global memoryMap
    first = quad[1]
    print(first)
    return i+1

# Solución a la escritura de una expresión (es el temporal de dicha expresión)
def an_write(quad, i):
    global memoryMap
    first = quad[1]
    addressFirst = ''

    if(isinstance(first, str)):
        lastCharacter = first[-1]
        if(lastCharacter == 'ç' or lastCharacter == '$'):
            first = first[0:len(first)-1]
            if(first.find('[') == -1):
                addressFirst = int(first)
            else:
                leftsqbrack = first.find('[')
                substr = first[0:leftsqbrack]
                dash = substr.find('-')
                firstAdd = substr[0:dash]
                secondAdd = substr[dash+1:len(substr)]
                firstAdd = int(firstAdd)
                secondAdd = int(secondAdd)
                indexAdd = first[leftsqbrack+1:len(first)-1]
                size = int(secondAdd) - int(firstAdd)
                indexAdd = int(indexAdd)
                keyIndex = verifyAddress(indexAdd)
                valueIndex = memoryMap[keyIndex].getValue(indexAdd)
                if(valueIndex < 0 or valueIndex >= size):
                    print("Index out of range")
                    sys.exit()
                else:
                    firstAdd += valueIndex
                    addressFirst = firstAdd
    valueFirst = 0
    keyStackFirst = ''
    if(addressFirst != ''):
        keyStackFirst = verifyAddress(addressFirst)
        valueFirst = memoryMap[keyStackFirst].getValue(addressFirst)
    else:
        valueFirst = first
    print(valueFirst)

    return i

# Cambio de índice para el diccionario de cuádruplos
def an_GotoT(quad, i):
    i = int(quad[1])
    i -= 1
    return i

# Solución al salto en falso
def an_GotoF(quad, i):
    global memoryMap
    first = quad[1]
    second = int(quad[2])
    addressFirst = ''

    if(isinstance(first, str)):
        lastCharacter = first[-1]
        if(lastCharacter == '$'):
            first = first[0:len(first)-1]
            addressFirst = int(first)
        else:
            print("Error")
            sys.exit()
    valueFirst = 0
    keyStackFirst = ''
    if(addressFirst != ''):
        keyStackFirst = verifyAddress(addressFirst)
        valueFirst = memoryMap[keyStackFirst].getValue(addressFirst)
    else:
        valueFirst = True
    

    if(valueFirst == False):
        i = second
        i -= 1
    return i

# Solución a la asignación
def an_assignment(quad, i):
    global memoryMap
    first = quad[1]
    second = quad[2]
    addressFirst = ''
    addressSecond = ''

    if(isinstance(second, str)):
        lastCharacter = second[-1]
        if(lastCharacter == 'ç' or lastCharacter == '$'):
            second = second[0:len(second)-1]
            if(second.find('[') == -1):
                addressSecond = int(second)
            else:
                leftsqbrack = second.find('[')
                substr = second[0:leftsqbrack]
                dash = substr.find('-')
                firstAdd = substr[0:dash]
                firstAdd = int(firstAdd)
                secondAdd = substr[dash+1:len(substr)]
                secondAdd = int(secondAdd)
                indexAdd = second[leftsqbrack+1:len(second)-1]
                size = int(secondAdd) - int(firstAdd)
                indexAdd = int(indexAdd)
                keyIndex = verifyAddress(indexAdd)
                valueIndex = memoryMap[keyIndex].getValue(indexAdd)
                if(valueIndex < 0 or valueIndex >= size):
                    print("Index out of range")
                    sys.exit()
                else:
                    firstAdd += valueIndex
                    addressSecond = firstAdd
    valueSecond = 0
    keyStackSecond = ''
    if(addressSecond != ''):
        keyStackSecond = verifyAddress(addressSecond)
        valueSecond = memoryMap[keyStackSecond].getValue(addressSecond)
    else:
        valueSecond = int(second)

    if(isinstance(first, str)):
        lastCharacter = first[-1]
        if(lastCharacter == 'ç' or lastCharacter == '$'):
            first = first[0:len(first)-1]
            if(first.find('[') == -1):
                addressFirst = int(first)
            else:
                leftsqbrack = first.find('[')
                substr = first[0:leftsqbrack]
                dash = substr.find('-')
                firstAdd = substr[0:dash]
                firstAdd = int(firstAdd)
                secondAdd = substr[dash+1:len(substr)]
                secondAdd = int(secondAdd)
                indexAdd = first[leftsqbrack+1:len(first)-1]
                size = int(secondAdd) - int(firstAdd)
                indexAdd = int(indexAdd)
                keyIndex = verifyAddress(indexAdd)
                valueIndex = memoryMap[keyIndex].getValue(indexAdd)
                if(valueIndex < 0 or valueIndex >= size):
                    print("Index out of range")
                    sys.exit()
                else:
                    firstAdd += valueIndex
                    addressFirst = firstAdd
    keyStackFirst = verifyAddress(addressFirst)
    memoryMap[keyStackFirst].setValue(addressFirst,  valueSecond)
    return i

# Solución a una expresión
def an_expression(quad, i):
    global memoryMap
    operator = quad[0]
    first = quad[1]
    second = quad[2]
    third = quad[3]
    addressFirst = ''
    addressSecond = ''
    addressThird = ''
    
    if(isinstance(first, str)):
        lastCharacter = first[-1]
        if(lastCharacter == 'ç' or lastCharacter == '$'):
            first = first[0:len(first)-1]
            if(first.find('[') == -1):
                addressFirst = int(first)
            else:
                leftsqbrack = first.find('[')
                substr = first[0:leftsqbrack]
                dash = substr.find('-')
                firstAdd = substr[0:dash]
                secondAdd = substr[dash+1:len(substr)]
                firstAdd = int(firstAdd)
                secondAdd = int(secondAdd)
                indexAdd = first[leftsqbrack+1:len(first)-1]
                size = int(secondAdd) - int(firstAdd)
                indexAdd = int(indexAdd)
                keyIndex = verifyAddress(indexAdd)
                valueIndex = memoryMap[keyIndex].getValue(indexAdd)
                if(valueIndex < 0 or valueIndex >= size):
                    print("Index out of range")
                    sys.exit()
                else:
                    firstAdd += valueIndex
                    addressFirst = firstAdd
    valueFirst = 0
    keyStackFirst = ''
    if(addressFirst != ''):
        keyStackFirst = verifyAddress(addressFirst)
        valueFirst = memoryMap[keyStackFirst].getValue(addressFirst)
    else:
        valueFirst = int(first)
    
    if(isinstance(second, str)):
        lastCharacter = second[-1]
        if(lastCharacter == 'ç' or lastCharacter == '$'):
            second = second[0:len(second)-1]
            if(second.find('[') == -1):
                addressSecond = int(second)
            else:
                leftsqbrack = second.find('[')
                substr = second[0:leftsqbrack]
                dash = substr.find('-')
                firstAdd = substr[0:dash]
                secondAdd = substr[dash+1:len(substr)]
                firstAdd = int(firstAdd)
                secondAdd = int(secondAdd)
                indexAdd = second[leftsqbrack+1:len(second)-1]
                size = int(secondAdd) - int(firstAdd)
                indexAdd = int(indexAdd)
                keyIndex = verifyAddress(indexAdd)
                valueIndex = memoryMap[keyIndex].getValue(indexAdd)
                if(valueIndex < 0 or valueIndex >= size):
                    print("Index out of range")
                    sys.exit()
                else:
                    firstAdd += valueIndex
                    addressSecond = firstAdd
    valueSecond = 0
    keyStackSecond = ''
    if(addressSecond != ''):
        keyStackSecond = verifyAddress(addressSecond)
        valueSecond = memoryMap[keyStackSecond].getValue(addressSecond)
    else:
        valueSecond = int(second)

    third = third[0:len(third)-1]
    addressThird = int(third)
    valueThird = 0
    keyStackThird = verifyAddress(addressThird)

    if(operator == '+'):
        valueThird = valueFirst + valueSecond
    elif(operator == '-'):
        if(isinstance(valueFirst, list)):
            quad1 = valueFirst
            init(quad1, memoryMap, i)
        else:
            valueThird = valueFirst - valueSecond
    elif(operator == '*'):
        valueThird = valueFirst * valueSecond
    elif(operator == '/'):
        valueThird = valueFirst / valueSecond
    elif(operator == '<'):
        valueThird = (valueFirst < valueSecond)
    elif(operator == '>'):
        valueThird = (valueFirst > valueSecond)
    elif(operator == '!='):
        valueThird = (valueFirst != valueSecond)
    elif(operator == '=='):
        valueThird = (valueFirst == valueSecond)
    elif(operator == '&'):
        valueThird = (valueFirst and valueSecond)
    elif(operator == '|'):
        valueThird = (valueFirst or valueSecond)
    memoryMap[keyStackThird].setValue(addressThird,  valueThird)
    return i

# Caso de error, solo regresa el índice, hay casos que el cuádruplo está vacío o contiene información basura
def error(quad, i):
    return i

# Función que tiene el switch para el tipo de solución
def switchQuad(estatuto, i):
    global memoryMap
    quad = estatuto
    operator = quad[0]
    switch_statute = {
        '+' : an_expression,
        '-' : an_expression,
        '*' : an_expression,
        '/' : an_expression,
        '<' : an_expression,
        '>' : an_expression,
        '!=' : an_expression,
        '==' : an_expression,
        '&' : an_expression,
        '|' : an_expression,
        '=' : an_assignment,
        'GotoF' : an_GotoF,
        'GotoT' : an_GotoT,
        'writeExp' : an_write,
        'writeStr' : an_writeStr,
        'read' : an_read,
        'average' : an_average,
        'variance' : an_variance,
        'mode' : an_mode,
        'plot' : an_plot,
        'regression' : an_regression,
        'retrieve' : an_retrieve,
        'return' : an_return
    }
    i = switch_statute.get(operator, error)(quad, i)
    return i

# Función inicial que recibe el cuádruplo, el mapa de memoria virtual y el índice; regresa los últimos dos (por cambios)
def init(estatuto, memoriaVirtual, i):
    global memoryMap
    memoryMap = memoriaVirtual
    i = switchQuad(estatuto, i)
    return ([memoryMap, i])