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

import sys

pila = []
contador = 1

def assignPriority(operador):
    priority = 1
    if(operador == '*' or operador == '/'):
        priority = 1
    elif(operador == '+' or operador == '-'):
        priority = 2
    elif(operador == '<' or operador == '>' or operador == '!=' or operador == '=='):
        priority = 3
    else:
        priority = 4
    return priority

def quickGen(expresion):
    global contador
    global pila
    data1 = expresion[0]
    operador = expresion[1]
    data2 = expresion[2]
    temp = 't' + str(contador)
    contador += 1
    quad = [operador, data1, data2, temp]
    return quad

def insideBrackets(prototype):
    global pila
    first = prototype[0]
    if(first == '-]-'):
        del prototype[0]
        return prototype
    second = prototype[1]
    if(second != '-]-'):
        if(second != '-[-'):
            third = prototype[2]
            if(third != '('):
                fourth = prototype[3]
                if(fourth != '-]-'):
                    if(fourth != '-[-'):
                        priority1 = assignPriority(second)
                        priority2 = assignPriority(fourth)
                        if(priority1 < priority2):
                            stack = [first, second, third]
                            quad = quickGen(stack)
                            pila += [quad]
                            del prototype[0]
                            del prototype[0]
                            prototype[0] = quad[-1]
                            prototype = insideBrackets(prototype)
                        else:
                            fifth = prototype[4]
                            if(fifth != '('):
                                sixth = prototype[5]
                                if(sixth != '-[-'):
                                    stack = [third, fourth, fifth]
                                    quad = quickGen(stack)
                                    pila += [quad]
                                    del prototype[2]
                                    del prototype[2]
                                    prototype[2] = quad[-1]
                                    prototype = insideBrackets(prototype)
                                else:
                                    nwPrototype = prototype
                                    save = [first, second]
                                    del nwPrototype[0]
                                    del nwPrototype[0]
                                    del nwPrototype[0]
                                    del nwPrototype[0]
                                    del nwPrototype[0]
                                    del nwPrototype[0]
                                    ID = fifth
                                    nwPrototype = insideBrackets(nwPrototype)
                                    last = pila[-1]
                                    temp = last[-1]
                                    salida = ID + '[' + temp + ']'
                                    prototype = save + [salida] + nwPrototype
                                    stack = [third, fourth, fifth]
                                    quad = quickGen(stack)
                                    del prototype[2]
                                    del prototype[2]
                                    prototype[2] = quad[-1]
                                    prototype = insideBrackets(prototype)
                            else:
                                nwPrototype = prototype
                                stack = [first, second, third, fourth]
                                del nwPrototype[0]
                                del nwPrototype[0]
                                del nwPrototype[0]
                                del nwPrototype[0]
                                del nwPrototype[0]
                                nwPrototype = insideParen(nwPrototype)
                                prototype = stack + nwPrototype
                                prototype = insideParen(prototype)
                    else:
                        nwPrototype = prototype
                        save = [first, second]
                        ID = third
                        del nwPrototype[0]
                        del nwPrototype[0]
                        del nwPrototype[0]
                        del nwPrototype[0]
                        nwPrototype = insideBrackets(nwPrototype)
                        last = pila[-1]
                        temp = last[-1]
                        salida = ID + '[' + temp + ']'
                        prototype = save + [salida] + nwPrototype
                        prototype = insideBrackets(prototype)
                else:
                    stack = [first, second, third]
                    quad = quickGen(stack)
                    pila += [quad]
                    del prototype[0]
                    del prototype[0]
                    prototype[0] = quad[-1]
                    prototype = insideBrackets(prototype)
            else:
                stack = [first, second]
                nwPrototype = prototype
                del nwPrototype[0]
                del nwPrototype[0]
                del nwPrototype[0]
                nwPrototype = insideParen(nwPrototype)
                prototype = insideBrackets(nwPrototype)
        else:
            nwPrototype = prototype
            ID = first
            del nwPrototype[0]
            del nwPrototype[0]
            nwPrototype = insideeBrackets(nwPrototype)
            last = pila[-1]
            temp = last[-1]
            salida = ID + '[' + temp + ']'
            prototype = [salida] + nwPrototype
            prototype = insideBrackets(prototype)
    else:
        stack = [first, '*', '1']
        quad = quickGen(stack)
        pila += [quad]
        del prototype[0]
        del prototype[0]
    return prototype

def insideParen(prototype):
    global pila
    first = prototype[0]
    second = prototype[1]
    if(second == ')'):
        del prototype[1]
        return prototype
    elif(second == '-[-'):
        nwPrototype = prototype
        ID = first
        del nwPrototype[0]
        del nwPrototype[0]
        nwPrototype = insideBrackets(nwPrototype)
        last = pila[-1]
        temp = last[-1]
        salida = ID + '[' + temp  + ']'
        prototype = [salida] + nwPrototype
        prototype = insideParen(prototype)
    else:
        third = prototype[2]
        if(third != '('):
            fourth = prototype[3]
            if(fourth != ')'):
                if(fourth != '-[-'):
                    priority1 = assignPriority(second)
                    priority2 = assignPriority(fourth)
                    if(priority1 < priority2):
                        stack = [first, second, third]
                        quad = quickGen(stack)
                        pila += [quad]
                        del prototype[0]
                        del prototype[0]
                        prototype[0] = quad[-1]
                        prototype = insideParen(prototype)
                    else:
                        fifth = prototype[4]
                        if(fifth != '('):
                            stack = [third, fourth, fifth]
                            quad = quickGen(stack)
                            pila += [quad]
                            del prototype[2]
                            del prototype[2]
                            prototype[2] = quad[-1]
                            prototype = insideParen(prototype)
                        else:
                            nwPrototype = prototype
                            stack = [first, second, third, fourth]
                            del nwPrototype[0]
                            del nwPrototype[0]
                            del nwPrototype[0]
                            del nwPrototype[0]
                            del nwPrototype[0]
                            nwPrototype = insideParen(nwPrototype)
                            prototype = stack + nwPrototype
                            prototype = insideParen(prototype)
                else:
                    stack = [first, second]
                    ID = third
                    nwPrototype = prototype
                    del nwPrototype[0]
                    del nwPrototype[0]
                    del nwPrototype[0]
                    del nwPrototype[0]
                    nwPrototype = insideBrackets[nwPrototype]
                    last = pila[-1]
                    temp = last[-1]
                    salida = ID + '[' + temp + ']'
                    prototype = stack + [salida] + nwPrototype
                    prototype = insideParen(prototype)
            else:
                stack = [first, second, third]
                quad = quickGen(stack)
                pila += [quad]
                del prototype[0]
                del prototype[0]
                del prototype[0]
                prototype[0] = quad[-1]
        else:
            stack = [first, second]
            nwPrototype = prototype
            del nwPrototype[0]
            del nwPrototype[0]
            del nwPrototype[0]
            nwPrototype = insideParen(nwPrototype)
            prototype = stack + nwPrototype
            prototype = insideParen(prototype)
    return prototype

def begin(expresion):
    global pila
    global contador
    if(len(expresion) == 1 and len(pila) == 0):
        if(isinstance(expresion[0], list) != True):
            pila = expresion
        else:
            if(expresion[0][0] != 'average' and expresion[0][0] != 'mode' and expresion[0][0] != 'variance'):
                calling = expresion[0]
                ID = calling[1]
                del calling[0]
                del calling[0]
                for i in calling:
                    stack = begin(i)
                    newQuad = ['param', stack[0], ID]
                    pila += [newQuad]
                temp = 't'+ str(contador)
                newQuad = ['retrieve', ID, temp]
                contador += 1
                pila += [newQuad]
                expresion = [temp]
            else:
                expresion[0] = expresion[0] + ['t' + str(contador)]
                contador += 1
                pila = expresion
                return pila
    elif(len(expresion) == 1 and len(pila) != 0):
        '''
        no se hace nada
        '''
    elif(len(expresion) == 3):
        quad = quickGen(expresion)
        pila += [quad]
        del expresion[0]
        del expresion[0]
        last = pila[-1]
        temp = last[-1]
        expresion[0] = temp 
    else:
        data1 = expresion[0]
        second = expresion[1]
        if(second != '-[-'):
            operador = expresion[1]
            data2 = expresion[2]
            if(data2 != '('):
                operador2 = expresion[3]
                if(operador2 != '-[-'):
                    priority1 = assignPriority(operador)
                    priority2 = assignPriority(operador2)
                    if(priority1 <= priority2):
                        stack = [data1, operador, data2]
                        del expresion[0]
                        del expresion[0]
                        quad = quickGen(stack)
                        expresion[0] = quad[-1]
                        pila += [quad]
                        expresion = begin(expresion)
                    else:
                        data3 = expresion[4]
                        if(data3 != '('):
                            stack = [data2, operador2, data3]
                            del expresion[2]
                            del expresion[2]
                            quad = quickGen(stack)
                            expresion[2] = quad[-1]
                            pila += [quad]
                            expresion = begin(expresion)
                        else:
                            stack = [data1, operador, data2, operador2]
                            prototype = expression
                            del prototype[0]
                            del prototype[0]
                            del prototype[0]
                            del prototype[0]
                            del prototype[0]
                            expresion = insideParen(prototype)
                            expresion = stack + expresion
                            expresion = begin(expresion)
                else:
                    stack = [data1, operador]
                    del expresion[0]
                    del expresion[0]
                    del expresion[0]
                    del expresion[0]
                    expresion = insideBrackets(expresion)
                    last = pila[-1]
                    temp = last[-1]
                    salida = data2 + '[' + temp + ']'
                    expresion = stack + [salida] + expresion
                    expresion = begin(expresion)
            else:
                stack = [data1, operador]
                prototype = expresion
                del prototype[0]
                del prototype[0]
                del prototype[0]
                expresion = insideParen(prototype)
                expresion = stack + expresion
                expresion = begin(expresion)
        else:
            del expresion[0]
            del expresion[0]
            expresion = insideBrackets(expresion)
            last = pila[-1]
            temp = last[-1]
            salida = data1 + '[' + temp + ']'
            expresion = [salida] + expresion
            expresion = begin(expresion)
    return expresion

def init(expresion, cont):
    global pila
    global contador
    contador = cont
    eraQuad = []
    try:
        if(expresion[0][0] == 'era'):
            eraQuad = expresion[0]
            del expresion[0]
            pila += [aQuad]
            contador += 1
    except:
        do = "nothing"
    expresion = begin(expresion)
    pila = [eraQuad] + pila
    return [pila, expresion, contador]