# -----------------------------------------------------------------------------
# millenium.py
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
from classMemory import *
from classVariables import *
from cuboSemantico import cuboSemantico
import severen as severen

memoryMap = {}
dictionaryVarG = {}
dictionaryStatutes = {}
dictionaryFunctions = {}
dictionaryAddress = {}
dictionaryAddressTemp = {}
sizeInt = 1000
inicioInt = 8000
inicioTempInt = 1000
sizeFloat = 1000
inicioFloat = 9000
inicioTempFloat = 2000
sizeChar = 1000
inicioChar = 10000
inicioTempChar = 3000
sizeBool = 500
inicioTempBool = 4000

def asignarEspacioParametro(IDParametro, tipo):
    global memoryMap
    address = ''
    if(tipo == 'int'):
        address = memoryMap['globalInt'].assignRegularSpace()
    elif(tipo == 'float'):
        address = memoryMap['globalFloat'].assignRegularSpace()
    elif(tipo == 'char'):
        address = memoryMap['globalChar'].assignRegularSpace()
    else:
        print("Imposible")
        sys.exit()
    stack = [IDParametro, address]
    return stack

def asignarEspacioTemporal(ID, tipo):
    global dictionaryAddressTemp
    global memoryMap
    address = ''
    if(tipo == 'int'):
        address = memoryMap['tempInt'].assignRegularSpace()
    elif(tipo == 'float'):
        address = memoryMap['tempFloat'].assignRegularSpace()
    elif(tipo == 'char'):
        address = memoryMap['tempChar'].assignRegularSpace()
    elif(tipo == 'bool'):
        address = memoryMap['tempBool'].assignRegularSpace()
    dictionaryAddressTemp[ID] = address

def isItValid(typeParameter, typeData):
    if(typeParameter != typeData):
        print("Los parametros no coinciden")
        sys.exit()

def an_parametro(quad, i, IDparametros, contParametro):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    tipoFirst = ''
    parametros = IDparametros.keys()
    arrParametros = []
    for j in parametros:
        arrParametros += [j]
    if(contParametro > (len(arrParametros) -1)):
        print("Se exedió en número de parametros")
        sys.exit()
    IDparametro = arrParametros[contParametro]
    tipoParametro = IDparametros[IDparametro].tipo
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
            isItValid(tipoParametro, tipoFirst)
        elif(first[0] == '\''):
            tipoFirst = 'char'
            isItValid(tipoParametro, tipoFirst)
        elif(first[0] == 't' and first[1].isnumeric()):
            address = dictionaryAddressTemp[first]
            quad[1] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoFirst = 'int'
            elif(address >= 2000 and address < 3000):
                tipoFirst = 'float'
            elif(address >= 3000 and address < 4000):
                tipoFirst = 'char'
            else:
                print("No existen los parametros booleanos")
                sys.exit()
            isItValid(tipoParametro, tipoFirst)
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            if(first.find('.', 0, len(first)) != -1):
                first = float(first)
                quad[1] = first
                tipoFirst = 'float'
            else:
                first = int(first)
                quad[1] = first
                tipoFirst = 'int'
            isItValid(tipoParametro, tipoFirst)
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        pos1 = first.find('[', 0, len(first))
        pos2 = first.find(']', 0, len(first))
        index = first[pos1+1: pos2]
        ID = first[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            tipoFirst = dictionaryVarG[ID].tipo
            quad[1] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
            isItValid(tipoParametro, tipoFirst)
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    stack = asignarEspacioParametro(IDparametro, tipoFirst)
    return stack

def an_era(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryFunctions
    global dictionaryStatutes
    eraID = i
    i += 1
    functionID = quad[1]
    IDs = dictionaryFunctions.keys()
    if(functionID in IDs):
        funcion = '''si existe'''
    else:
        print("La funcion: " + functionID + " no existe")
        sys.exit()
    obj = dictionaryFunctions[functionID]
    direcciones = {}
    flag = False
    contParametro = 0
    while(not flag):
        quad = dictionaryStatutes[i]
        inst = quad[0]
        if(inst == '+' or inst == '-' or inst == '*' or inst == '/'):
            an_regularExpression(quad, i)
        elif(inst == 'param'):
            stack = an_parametro(quad, i, obj.parametros, contParametro)
            IDParametro = stack[0]
            direccion = stack[1]
            direcciones[IDParametro] = direccion
            quad[2] = str(direccion) + 'ç'
            dictionaryStatutes[i] = quad
            contParametro += 1
        elif(inst == 'era'):
            i = an_era(quad, i)
        elif(inst == 'callFunction'):
            if(obj.especie != 'Void'):
                print("Es una funcion de retorno")
                sys.exit()
            stack = severen.init(obj.parametros, memoryMap, dictionaryVarG, dictionaryStatutes, dictionaryFunctions, dictionaryAddress, obj, i, direcciones)
            dictionaryStatutes = stack[1]
            i = stack[0]
            memoryMap = stack[2]
            return i
        elif(inst == 'retrieve'):
            if(obj.especie == "Retorno"):
                functionSt = obj.estatutos
                keysFuncSt = functionSt.keys()
                lastKeyFuncSt = keysFuncSt[-1]
                lastQuadFuncSt = functionSt[lastKeyFuncSt]
                if(lastQuadFuncSt[0] != 'return'):
                    print("La función no tiene un estatuto de retorno al final")
                    sys.exit()
                stack = severen.init(obj.parametros, memoryMap, dictionaryVarG, dictionaryStatutes, dictionaryFunctions, dictionaryAddress, obj, i, direcciones)
                dictionaryStatutes = stack[1]
                i = stack[0]
                memoryMap = stack[2]
                return i
            else:
                print("La función " + obj.ID +  " no es de tipo retorno")
        i += 1
        flag = (inst == 'callFunction' or inst == 'retrieve')

def an_modeFunc(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            if(dictionaryVarG[first].especie != "Arreglo"):
                print("Debe ser un arreglo")
                sys.exit()
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            print("Imposible")
            sys.exit()
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        print("No se puede con el indice de una variable")
        sys.exit()
    temp = quad[2]
    tipo = tipoFirst
    asignarEspacioTemporal(temp, tipo)
    address = dictionaryAddressTemp[temp]
    quad[2] = str(address) + '$'
    dictionaryStatutes[i] = quad

def an_specialFunc(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            if(dictionaryVarG[first].especie != "Arreglo"):
                print("Debe ser un arreglo")
                sys.exit()
            address = dictionaryAddress[first]
            quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            print("Imposible")
            sys.exit()
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        print("No se puede con el indice de una variable")
        sys.exit()
    if(tipoFirst == 'int' or tipoFirst == "float"):
        temp = quad[2]
        tipo = tipoFirst
        asignarEspacioTemporal(temp, tipo)
        address = dictionaryAddressTemp[temp]
        quad[2] = str(address) + '$'
    else:
        print("La variable debe ser entera o flotante para el promedio o varianza")
        sys.exit()
    dictionaryStatutes[i] = quad

def an_read(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address) + 'ç'
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            print("Imposible")
            sys.exit()
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        pos1 = first.find('[', 0, len(first))
        pos2 = first.find(']', 0, len(first))
        index = first[pos1+1: pos2]
        ID = first[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            quad[1] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    dictionaryStatutes[i] = quad

def an_writeExpression(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryStatutes
    IDs = dictionaryVarG.keys()
    first = quad[1]
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address) + 'ç'
        elif(first[0] == '\''):
            nothing = '''tipoFirst = 'char'''
        elif(first[0] == 't' and first[1].isnumeric()):
            address = dictionaryAddressTemp[first]
            quad[1] = str(address) + '$'
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            if(first.find('.', 0, len(first)) != -1):
                first = float(first)
                quad[1] = first
            else:
                first = int(first)
                quad[1] = first
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        pos1 = first.find('[', 0, len(first))
        pos2 = first.find(']', 0, len(first))
        index = first[pos1+1: pos2]
        ID = first[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            quad[1] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    dictionaryStatutes[i] = quad

def an_regression(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            if(dictionaryVarG[first].especie != "Arreglo"):
                print("La variable: " + first + " no es arreglo")
                sys.exit()
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            address = dictionaryAddressTemp[first]
            quad[1] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoFirst = 'int'
            elif(address >= 2000 and address < 3000):
                tipoFirst = 'float'
            elif(address >= 3000 and address < 4000):
                tipoFirst = 'char'
            else:
                tipoFirst = 'bool'
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        print("Imposible")
        sys.exit()
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDs):
            if(dictionaryVarG[second].especie != "Arreglo"):
                print("La variable: " + second + " no es arreglo")
                sys.exit()
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[second]
            quad[2] = str(address[0]) + '-' + str(address[1]) + 'ç'
            tipoSecond = dictionaryVarG[second].tipo
        elif(len(second) == 1 and second.isnumeric() == False):
            print("Imposible")
            sys.exit()
        elif(second[0] == 't' and second[1].isnumeric()):
            address = dictionaryAddressTemp[second]
            quad[2] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoSecond = 'int'
            elif(address >= 2000 and address < 3000):
                tipoSecond = 'float'
            elif(address >= 3000 and address < 4000):
                tipoSecond = 'char'
            else:
                tipoSecond = 'bool'
        elif(second.isnumeric() or second.find('.', 0, len(second)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + second + " no ha sido definido")
            sys.exit()
    else:
        print("Imposible")
        sys.exit()
    if(tipoFirst != 'int' or tipoSecond != 'int'):
        print("Imposible")
        sys.exit()
    dictionaryStatutes[i] = quad

def an_jumpFalse(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    IDs = dictionaryVarG.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            print("No existen las variables booleanas")
            sys.exit()
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            address = dictionaryAddressTemp[first]
            quad[1] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoFirst = 'int'
            elif(address >= 2000 and address < 3000):
                tipoFirst = 'float'
            elif(address >= 3000 and address < 4000):
                tipoFirst = 'char'
            else:
                tipoFirst = 'bool'
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        print("Imposible")
        sys.exit()
    if(tipoFirst != 'bool'):
        print("El resultado de la expresión debe ser booleano")
        sys.exit()
    dictionaryStatutes[i] = quad

def an_equalExpression(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryStatutes
    IDs = dictionaryVarG.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
        elif(first[0] == '\''):
            print("Imposible")
            sys.exit()
        elif(first[0] == 't' and first[1].isnumeric()):
            print("Imposible")
            sys.exit()
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            print("Imposible")
            sys.exit()
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        pos1 = first.find('[', 0, len(first))
        pos2 = first.find(']', 0, len(first))
        index = first[pos1+1: pos2]
        ID = first[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            tipoFirst = dictionaryVarG[ID].tipo
            quad[1] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[second]
            quad[2] = str(address) + 'ç'
            tipoSecond = dictionaryVarG[second].tipo
        elif(len(second) == 1 and second.isnumeric() == False):
            tipoSecond = 'char'
        elif(second[0] == 't' and second[1].isnumeric()):
            address = dictionaryAddressTemp[second]
            quad[2] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoSecond = 'int'
            elif(address >= 2000 and address < 3000):
                tipoSecond = 'float'
            elif(address >= 3000 and address < 4000):
                tipoSecond = 'char'
            else:
                tipoSecond = 'bool'
        elif(second.isnumeric() or second.find('.', 0, len(second)) != -1):
            if(second.find('.', 0, len(second)) != -1):
                second = float(second)
                quad[2] = second
                tipoSecond = 'float'
            else:
                second = int(second)
                quad[2] = second
                tipoSecond = 'int'
        else:
            print("Este ID: " + second + " no ha sido definido")
            sys.exit()
    else:
        pos1 = second.find('[', 0, len(second))
        pos2 = second.find(']', 0, len(second))
        index = second[pos1+1: pos2]
        ID = second[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            tipoSecond = dictionaryVarG[ID].tipo
            quad[2] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    isIt = cuboSemantico[quad[0]][tipoFirst][tipoSecond]
    if(isIt[0] != True):
        print("Operación no válida")
        sys.exit()        
    dictionaryStatutes[i] = quad

def an_regularExpression(quad, i):
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryStatutes
    IDs = dictionaryVarG.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[first]
            quad[1] = str(address) + 'ç'
            tipoFirst = dictionaryVarG[first].tipo
        elif(first[0] == '\''):
            tipoFirst = 'char'
        elif(first[0] == 't' and first[1].isnumeric()):
            address = dictionaryAddressTemp[first]
            quad[1] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoFirst = 'int'
            elif(address >= 2000 and address < 3000):
                tipoFirst = 'float'
            elif(address >= 3000 and address < 4000):
                tipoFirst = 'char'
            else:
                tipoFirst = 'bool'
        elif(first.isnumeric() or first.find('.', 0, len(first)) != -1):
            if(first.find('.', 0, len(first)) != -1):
                first = float(first)
                quad[1] = first
                tipoFirst = 'float'
            else:
                first = int(first)
                quad[1] = first
                tipoFirst = 'int'
        else:
            print("Este ID: " + first + " no ha sido definido")
            sys.exit()
    else:
        pos1 = first.find('[', 0, len(first))
        pos2 = first.find(']', 0, len(first))
        index = first[pos1+1: pos2]
        ID = first[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            tipoFirst = dictionaryVarG[ID].tipo
            quad[1] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDs):
            keysMemory = dictionaryAddress.keys()
            address = dictionaryAddress[second]
            quad[2] = str(address) + 'ç'
            tipoSecond = dictionaryVarG[second].tipo
        elif(second[0] == '\''):
            tipoSecond = 'char'
        elif(second[0] == 't' and second[1].isnumeric()):
            address = dictionaryAddressTemp[second]
            quad[2] = str(address) + '$'
            if(address >= 1000 and address < 2000):
                tipoSecond = 'int'
            elif(address >= 2000 and address < 3000):
                tipoSecond = 'float'
            elif(address >= 3000 and address < 4000):
                tipoSecond = 'char'
            else:
                tipoSecond = 'bool'
        elif(second.isnumeric() or second.find('.', 0, len(second)) != -1):
            if(second.find('.', 0, len(second)) != -1):
                second = float(second)
                quad[2] = second
                tipoSecond = 'float'
            else:
                second = int(second)
                quad[2] = second
                tipoSecond = 'int'
        else:
            print("Este ID: " + second + " no ha sido definido")
            sys.exit()
    else:
        pos1 = second.find('[', 0, len(second))
        pos2 = second.find(']', 0, len(second))
        index = second[pos1+1: pos2]
        ID = second[0:pos1]
        especie = dictionaryVarG[ID].especie
        if(especie == "Arreglo"):
            addressID = dictionaryAddress[ID]
            addresstemp = dictionaryAddressTemp[index]
            tipoSecond = dictionaryVarG[ID].tipo
            quad[2] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    isIt = cuboSemantico[quad[0]][tipoFirst][tipoSecond]
    if(isIt[0]):
        temp = quad[3]
        tipo = isIt[1]
        asignarEspacioTemporal(temp, tipo)
        address = dictionaryAddressTemp[temp]
        quad[3] = str(address) + '$'
    else:
        print("Operación no válida")
        sys.exit()
    dictionaryStatutes[i] = quad

def changeQuads():
    global dictionaryStatutes
    global dictionaryVarG
    global dictionaryAddress
    keys = dictionaryStatutes.keys()
    for i in keys:
        quad = dictionaryStatutes[i]
        inst = quad[0]
        if(inst == '+' or inst == '-' or inst == '*' or inst == '/' or inst == '<' or inst == '>' or inst == '!=' or inst == '==' or inst == '&' or inst == '|'):
            an_regularExpression(quad, i)
        elif(inst == '='):
            an_equalExpression(quad, i)
        elif(inst == 'GotoF'):
            an_jumpFalse(quad, i)
        elif(inst == 'plot' or inst == 'regression'):
            an_regression(quad, i)
        elif(inst == 'writeExp'):
            an_writeExpression(quad, i)
        elif(inst == 'read'):
            an_read(quad, i)
        elif(inst == 'average' or inst == 'variance'):
            an_specialFunc(quad, i)
        elif(inst == 'mode'):
            an_modeFunc(quad, i)
        elif(inst == 'return'):
            print("El programa principal no puede hacer return")
            sys.exit()
        elif(inst == 'era'):
            i = an_era(quad, i)
            keys = dictionaryStatutes.keys()
        elif(inst == 'return'):
            print("No puede haber return en el main")
            sys.exit()
    print(dictionaryStatutes)

def asignacionEspacio():
    global dictionaryVarG
    global memoryMap
    global dictionaryAddress
    keys = dictionaryVarG.keys()
    for i in keys:
        obj = dictionaryVarG[i]
        tipo = obj.tipo
        address = ''
        if(tipo == 'int'):
            address = memoryMap['globalInt'].assignSpace(obj)
        elif(tipo == 'float'):
            address = memoryMap['globalFloat'].assignSpace(obj)
        else:
            address = memoryMap['globalChar'].assignSpace(obj)
        dictionaryAddress[obj.ID] = address

def init(dictVarGlob, dictEstatutos, dictFunciones):
    global memoryMap
    global sizeInt
    global inicioInt
    global inicioTempInt
    global sizeFloat
    global inicioFloat
    global inicioTempFloat
    global sizeChar
    global inicioChar
    global inicioTempChar
    global dictionaryVarG
    global dictionaryStatutes
    global dictionaryFunctions
    dictionaryFunctions = dictFunciones
    dictionaryStatutes = dictEstatutos
    dictionaryVarG = dictVarGlob
    objInt = StackMemory('int', sizeInt, inicioInt, sizeInt + inicioInt)
    objFloat = StackMemory('float', sizeFloat, inicioFloat, sizeFloat + inicioFloat)
    objChar = StackMemory('char', sizeChar, inicioChar, sizeChar + inicioChar)
    memoryMap['globalInt'] = objInt
    memoryMap['globalFloat'] = objFloat
    memoryMap['globalChar'] = objChar
    objInt = StackMemory('int', sizeInt, inicioTempInt, sizeInt + inicioTempInt)
    objFloat = StackMemory('float', sizeFloat, inicioTempFloat, sizeFloat + inicioTempFloat)
    objChar = StackMemory('char', sizeChar, inicioTempChar, sizeChar + inicioTempChar)
    objBool = StackMemory('bool', sizeBool, inicioTempBool, sizeBool + inicioTempBool)
    memoryMap['tempInt'] = objInt
    memoryMap['tempFloat'] = objFloat
    memoryMap['tempChar'] = objChar
    memoryMap['tempBool'] = objBool
    asignacionEspacio()
    changeQuads()
    return [dictionaryStatutes, memoryMap]