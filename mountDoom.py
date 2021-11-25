# -----------------------------------------------------------------------------
# mountDoom.py
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

def an_return(quad, i):
    global memoryMap
    global waitingForReturn
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
        memoryMap[keyStackFirst].seetValue(temp, value)
    except:
        do = "nothing"

    return i

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

def calculateMode(stack):
    mode = mode(stack)
    return mode

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

def calculateVariance(stack):
    variance = np.var(stack)
    return variance

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

def calculateAvg(stack, size):
    acum = 0
    for h in stack:
        index = stack[h]
        acum += index
    avg = acum / size
    return avg

def an_average(quad, i):
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
    average = calculateAvg(stack, size)
    
    lastCharacter = second[-1]
    if(lastCharacter == 'ç' or lastCharacter == '$'):
        second = second[0:len(second)-1]
        addressSecond = int(second)
    keyStackSecond = verifyAddress(addressSecond)
    memoryMap[keyStackSecond].setValue(addressSecond, average)
    return i

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

    valueFirst = 0
    keyStackFirst = ''
    if(addressFirst != ''):
        keyStackFirst = verifyAddress(addressFirst)
        valueFirst = memoryMap[keyStackFirst].getValue(addressFirst)
    else:
        valueFirst = first
    print(valueFirst)
    
    return i

def an_writeStr(quad, i):
    global memoryMap
    first = quad[1]
    return i+1

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

    return i

def an_GotoT(quad, i):
    i = int(quad[1])
    return i

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
    return i

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
        valueSecond = second

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

def error(quad, i):
    return i

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

def init(estatuto, memoriaVirtual, i):
    global memoryMap
    memoryMap = memoriaVirtual
    i = switchQuad(estatuto, i)
    return ([memoryMap, i])