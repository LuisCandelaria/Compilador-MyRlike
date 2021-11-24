# -----------------------------------------------------------------------------
# severen.py
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
dictionaryVarLoc = {}
dictionaryParam = {}
dictionaryStatutes = {}
dictionaryStatutesFun = {}
dictionaryFunctions = {}
dictionaryAddress = {}
dictionaryAddressLoc = {}
dictionaryAddressParam = {}
dictionaryAddressTemp = {}
functionObj = []

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

def an_return(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    global dictionaryFunctions
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoFirst = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoFirst = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoFirst = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
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
    if(functionObj.tipo == tipoFirst):
        dictionaryStatutesFun[i] = quad
    else:
        print("El return no es del tipo correcto")
        sys.exit()

def isItValid(typeParameter, typeData):
    if(typeParameter != typeData):
        print("Los parametros no coinciden")
        sys.exit()

def an_parametro(quad, i, IDparametros, contParametro):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    global dictionaryFunctions
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
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
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
                keysMemory = dictionaryAddress.keys()
                address = dictionaryAddress[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarG[first].tipo
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
        pos1 = second.find('[', 0, len(second))
        pos2 = second.find(']', 0, len(second))
        index = second[pos1+1: pos2]
        ID = first[0:pos1]
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoSecond = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoSecond = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoSecond = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
            addresstemp = dictionaryAddressTemp[index]
            quad[2] = str(addressID[0]) + '-' + str(addressID[1]) + '[' + str(addresstemp) + ']' + 'ç'
            if(addresstemp >= 1000 and addresstemp < 2000):
                tipoTemp = '''tipoFirst = 'int'''
            else:
                print("El indice debe ser entero")
                sys.exit()
        else:
            print("La variable: " + ID + " no es un arreglo")
            sys.exit()
    dictionaryStatutesFun[i] = quad
    stack = asignarEspacioParametro(IDparametro, tipoFirst)
    return stack

def an_era(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    global dictionaryFunctions
    eraID = i
    i += 1
    functionID = quad[1]
    IDs = dictionaryFunctions.keys()
    if(functionID in IDs):
        function = '''si existe'''
    else:
        print("La función " + functionID + " no existe")
        sys.ext()
    obj = dictionaryFunctions[functionID]
    direcciones = {}
    #save progress
    auxDictParam = dictionaryParam
    auxDictVarLoc = dictionaryVarLoc
    auxDictAddressTemp = dictionaryAddressTemp
    auxDictAddressLoc = dictionaryAddressLoc
    auxDictAddressParam = dictionaryAddressParam
    auxDictStatutesFun = dictionaryStatutesFun
    auxfunctionObj = functionObj
    flag = False
    contParametro = 0
    while(not flag):
        quad = dictionaryStatutesFun[i]
        inst = quad[0]
        if(inst == '+' or inst == '-' or inst == '*' or inst == '/'):
            an_regularExpression(quad, i)
        elif(inst == 'param'):
            stack = an_parametro(quad, i, obj.parametros, contParametro)
            IDParametro = stack[0]
            direccion = stack[1]
            direcciones[IDParametro] = direccion
            quad[2] = str(direccion) + 'ç'
            dictionaryStatutesFun[i] = quad
            contParametro += 1
        elif(inst == 'era'):
            i = an_era(quad, i)
        elif(inst == 'callFunction'):
            if(obj.especie != 'Void'):
                print("Es una funcion de retorno")
                sys.exit()
            stack = severen.init(obj.parametros, memoryMap, dictionaryVarG, dictionaryStatutesFun, dictionaryFunctions, dictionaryAddress, obj, i, direcciones)
            dictionaryStatutesFun = stack[1]
            i = stack[0]
            memoryMap = stack[2]
            dictionaryParam = auxDictParam
            dictionaryVarLoc = auxDictVarLoc
            dictionaryAddressTemp = auxDictAddressTemp
            dictionaryAddressLoc = auxDictAddressLoc
            dictionaryAddressParam = auxDictAddressParam
            functionObj = auxfunctionObj
            return i
        elif(inst == 'retrieve'):
            if(obj.especie == "Retorno"):
                print("Se puede")
            else:
                print("La función " + obj.ID +  " no es de tipo retorno")
        i += 1
        flag = (inst == 'callFunction' or inst == 'retrieve')

def an_modeFunc(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                if(dictionaryParam[first].especie != "Arreglo"):
                    print("Debe ser un arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                if(dictionaryVarLoc[first].especie != "Arreglo"):
                    print("Debe ser un arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
    dictionaryStatutesFun[i] = quad

def an_specialFunc(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    tipoFirst = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                if(dictionaryParam[first].especie != "Arreglo"):
                    print("Debe ser un arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                if(dictionaryVarLoc[first].especie != "Arreglo"):
                    print("Debe ser un arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
    if(tipoFirst == 'int' or tipoFirst == "float"):
        temp = quad[2]
        tipo = tipoFirst
        asignarEspacioTemporal(temp, tipo)
        address = dictionaryAddressTemp[temp]
        quad[2] = str(address) + '$'
    else:
        print("La variable debe ser entera o flotante para el promedio o varianza")
        sys.exit()
    dictionaryStatutesFun[i] = quad

def an_read(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoFirst = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoFirst = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoFirst = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
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
    dictionaryStatutesFun[i] = quad

def an_writeExpression(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
                keysMemory = dictionaryAddress.keys()
                address = dictionaryAddress[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarG[first].tipo
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
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoFirst = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoFirst = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoFirst = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
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
    dictionaryStatutesFun[i] = quad

def an_regression(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                if(dictionaryParam[first].especie != "Arreglo"):
                    print("La variable: " + first + " no es arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                if(dictionaryVarLoc[first].especie != "Arreglo"):
                    print("La variable: " + first + " no es arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address[0]) + '-' + str(address[1]) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
        print("Imposible")
        sys.exit()
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDsGlob or second in IDsParam or second in IDsLoc):
            if(second in IDsParam):
                if(dictionaryParam[first].especie != "Arreglo"):
                    print("La variable: " + first + " no es arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[second]
                quad[2] = str(address[0]) + '-' + str(address[1])+ 'ç'
                tipoSecond = dictionaryParam[second].tipo
            elif(second in IDsLoc):
                if(dictionaryVarLoc[first].especie != "Arreglo"):
                    print("La variable: " + first + " no es arreglo")
                    sys.exit()
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[second]
                quad[2] = str(address[0]) + '-' + str(address[1])+ 'ç'
                tipoSecond = dictionaryVarLoc[second].tipo
            else:
                if(dictionaryVarG[first].especie != "Arreglo"):
                    print("La variable: " + first + " no es arreglo")
                    sys.exit()
                keysMemory = dictionaryAddress.keys()
                address = dictionaryAddress[second]
                quad[2] = str(address[0]) + '-' + str(address[1])+ 'ç'
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
        print("Imposible")
        sys.exit()
    if(tipoFirst != 'int' or tipoSecond != 'int'):
        print("Imposible")
        sys.exit()
    dictionaryStatutesFun[i] = quad

def an_jumpFalse(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
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
    dictionaryStatutesFun[i] = quad

def an_equalExpression(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoFirst = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoFirst = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoFirst = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
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
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDsGlob or second in IDsParam or second in IDsLoc):
            if(second in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[second]
                quad[2] = str(address) + 'ç'
                tipoSecond = dictionaryParam[second].tipo
            elif(second in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[second]
                quad[2] = str(address) + 'ç'
                tipoSecond = dictionaryVarLoc[second].tipo
            else:
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
        ID = first[0:pos1]
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoSecond = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoSecond = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoSecond = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
            addresstemp = dictionaryAddressTemp[index]
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
    dictionaryStatutesFun[i] = quad

def an_regularExpression(quad, i):
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressLoc
    global dictionaryAddressParam
    global dictionaryStatutesFun
    IDsGlob = dictionaryVarG.keys()
    IDsParam = dictionaryParam.keys()
    IDsLoc = dictionaryVarLoc.keys()
    first = quad[1]
    second = quad[2]
    tipoFirst = ''
    tipoSecond = ''
    if(first.find(']', 0, len(first)) == -1):
        if(first in IDsGlob or first in IDsParam or first in IDsLoc):
            if(first in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryParam[first].tipo
            elif(first in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[first]
                quad[1] = str(address) + 'ç'
                tipoFirst = dictionaryVarLoc[first].tipo
            else:
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
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoFirst = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoFirst = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoFirst = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
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
    if(second.find(']', 0, len(second)) == -1):
        if(second in IDsGlob or second in IDsParam or second in IDsLoc):
            if(second in IDsParam):
                keysMemory = dictionaryAddressParam.keys()
                address = dictionaryAddressParam[second]
                quad[2] = str(address) + 'ç'
                tipoSecond = dictionaryParam[second].tipo
            elif(second in IDsLoc):
                keysMemory = dictionaryAddressLoc.keys()
                address = dictionaryAddressLoc[second]
                quad[2] = str(address) + 'ç'
                tipoSecond = dictionaryVarLoc[second].tipo
            else:
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
        ID = first[0:pos1]
        especie = ''
        addressID = ''
        if(ID in IDsParam):
            especie = dictionaryParam[ID].especie
            tipoSecond = dictionaryParam[ID].tipo
            addressID = dictionaryAddressTemp[ID]
        elif(ID in IDsLoc):
            especie = dictionaryVarLoc[ID].especie
            tipoSecond = dictionaryVarLoc[ID].tipo
            addressID = dictionaryAddressLoc[ID]
        else:
            especie = dictionaryVarG[ID].especie
            tipoSecond = dictionaryVarG[ID].tipo
            addressID = dictionaryAddress[ID]
        if(especie == "Arreglo"):
            addresstemp = dictionaryAddressTemp[index]
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
    dictionaryStatutesFun[i] = quad

def changeQuads():
    global dictionaryStatutesFun
    global dictionaryVarG
    global dictionaryParam
    global dictionaryVarLoc
    global dictionaryAddress
    global dictionaryAddressLoc
    global dictionaryAddressParam
    keys = dictionaryStatutesFun.keys()
    for i in keys:
        quad = dictionaryStatutesFun[i]
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
            if(functionObj.especie != "Retorno"):
                an_return(quad, i)
            else:
                print("La función: " + functionObj.ID + " no es de tipo Retorno")
                sys.exit()
        elif(inst == 'era'):
            i = an_era(quad, i)
            keys = dictionaryStatutesFun.keys()

def asignacionEspacio():
    global dictionaryVarLoc
    global memoryMap
    global dictionaryAddressLoc
    keys = dictionaryVarLoc.keys()
    for i in keys:
        obj = dictionaryVarLoc[i]
        tipo = obj.tipo
        address = ''
        if(tipo == 'int'):
            address = memoryMap['globalInt'].assignSpace(obj)
        elif(tipo == 'float'):
            address = memoryMap['globalFloat'].assignSpace(obj)
        else:
            address = memoryMap['globalChar'].assignSpace(obj)
        dictionaryAddressLoc[obj.ID] = address

def fillStack(dictionary, keys):
    stack = []
    for i in keys:
        quad = dictionary[i]
        stack += [quad]
    return stack

def writeDictionary(stack):
    cont = 1
    dictionary = {}
    for i in stack:
        dictionary[cont] = i
        cont += 1
    return dictionary

def mergeDictionaries(first, second, third):
    keys1 = first.keys()
    keys2 = second.keys()
    keys3 = third.keys()
    stack1 = fillStack(first, keys1)
    stack2 = fillStack(second, keys2)
    stack3 = fillStack(third, keys3)
    finalStack = stack1 + stack2 + stack3
    dictionary = writeDictionary(finalStack)
    return dictionary

def init(dictParam, dictMemory, dictVarG, dictStatutes, dictFunctions, dictAddress, objFunction, i, direcciones):
    global memoryMap
    global dictionaryVarG
    global dictionaryVarLoc
    global dictionaryParam
    global dictionaryStatutes
    global dictionaryStatutesFun
    global dictionaryFunctions
    global dictionaryAddress
    global dictionaryAddressTemp
    global dictionaryAddressParam
    global functionObj
    memoryMap = dictMemory
    dictionaryVarG = dictVarG
    dictionaryParam = dictParam
    dictionaryStatutes = dictStatutes
    dictionaryFunctions = dictFunctions
    dictionaryAddress = dictAddress
    dictionaryAddressParam = direcciones
    functionObj = objFunction
    dictionaryStatutesFun = functionObj.estatutos
    dictionaryVarLoc = functionObj.variablesLocales
    asignacionEspacio()
    prevQuads = {}
    nextQuads = {}
    for j in range(1, i+1):
        prevQuads[j] = dictionaryStatutes[j]
    changeQuads()
    for k in range(i+1, len(dictionaryStatutes.keys())+1):
        nextQuads[k] = dictionaryStatutes[k]
    dictionaryStatutes = mergeDictionaries(prevQuads, dictionaryStatutesFun, nextQuads)
    keys = dictionaryStatutes.keys()
    pila = []
    for i in keys:
        pila += [i]
    lastKey = pila[-1]
    return[lastKey, dictionaryStatutes, memoryMap]