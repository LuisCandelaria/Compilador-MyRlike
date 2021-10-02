# -----------------------------------------------------------------------------
# analizadorSintactico.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
#
# Nota y comentarios:
# En este documento se podrá ver cómo están determinadas todas las palabras
# reservadas como por ejemplo 'Program', 'if', etc. así como los tokens que
# representan todos los caracteres o conjuntos de los mismos con una finalidad
# específica en el compilador, por ejemplo: ID que contiene letras y numeros,
# el simbolo { para el inicio de un bloque, etc.
#
# Indice:
# 1. Librerias
# 2. Tokens
# 3. Palabras reservadas
# 4. Expresiones regulares
# 5. Lexer
# 6. Funcion para pruebas (Una vez teniendo el analizador siintactico esta 
# funcion no se usará)
# -----------------------------------------------------------------------------

# Librerías necesarias para la ejecución del archivo
import ply.lex as lex
import re
import codecs
import os
import sys

# Lista de tokens
tokens = [
    'ID',
    'CTE_STRING',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_CHAR',
    'COLON',
    'SEMICOLON',
    'COMA',
    'LBRACK',
    'RBRACK',
    'LPAREN',
    'RPAREN',
    'LSBRACK',
    'RSBRACK',
    'DIFF',
    'EQUAL',
    'GTHAN',
    'LTHAN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    'AND',
    'OR'
]

# Palabras reservadas
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'vars' : 'VARS',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'function' : 'FUNCTION',
    'void' : 'VOID',
    'return' : 'RETURN',
    'read' : 'READ',
    'write' : 'WRITE',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO',
    'average' : 'AVERAGE',
    'mode' : 'MODE',
    'variance' : 'VARIANCE',
    'regression' : 'REGRESSION',
    'plotxy' : 'PLOTXY'
}

tokens = tokens + list(reserved.values())

# Expresiones regulares
t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_FLOAT = r'[0-9]+\.[0-9]+'
t_CTE_CHAR = r'(\'[^\']*\')'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMA = r'\,'
t_LBRACK = r'\{'
t_RBRACK = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSBRACK = r'\['
t_RSBRACK = r'\]'
t_DIFF = r'\<>'
t_EQUAL = r'\=='
t_GTHAN = r'\>'
t_LTHAN = r'\<'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'\='
t_AND = r'\&'
t_OR = r'\|'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') #Check reserved words
    return t

def t_CTE_INT(t):
    def t_CTE_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_newline(t):
    def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Lexer
lexer = lex.lex()

# Funcion que analiza un archivo de prueba
def f_analisisLexico(direccion):
    f = codecs.open(direccion, "r", "utf-8")
    data = f.read()
    f.close()
    f2 = open("lexico.txt", "a")
    # Give the lexer some input
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break   # No more input
        f2.write(str(tok) + '\n')
    f2.close()