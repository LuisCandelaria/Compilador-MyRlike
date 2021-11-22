# -------------------------------------
# cuboSemantico.py
# Version 1.0
#
# Luis Eugenio Candelaria Azpilcueta
# A00816826
# -------------------------------------

cuboSemantico = {
    '+' : {
        "int" : { 
            "int" : [True, "int"],
            "float" : [True, "float"],
            "char" : [False], 
            "string" : [False]
        },
        "float" : {
            "int" : [True, "float"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" : {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "string"], 
            "string" : [True, "string"]
        },
        "string" : {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "string"], 
            "string" : [True, "string"]
        }
    },
    '-' : {
        "int" :
        { 
            "int" : [True, "int"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "float"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        }
    },
    '*' : {
        "int" :
        { 
            "int" : [True, "int"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "float"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        }
    },
    '/' : {
        "int" :
        { 
            "int" : [True, "float"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "float"], 
            "float" : [True, "float"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        }
    },
    '==' : {
        "int" :
        { 
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "bool"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "bool"]
        }
    },
    '>' : {
        "int" :
        { 
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "bool"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "bool"]
        }
    },
    '<' : {
        "int" :
        { 
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "bool"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "bool"]
        }
    },
    '!=' : {
        "int" :
        { 
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "bool"], 
            "float" : [True, "bool"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "bool"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "bool"]
        }
    },
    '=' : {
        "int" :
        { 
            "int" : [True], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False],
            "bool" : [False]
        },
        "float" :
        {
            "int" : [False], 
            "float" : [True], 
            "char" : [False], 
            "string" : [False],
            "bool" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True], 
            "string" : [False],
            "bool" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True],
            "bool" : [False]
        }
    },
    '&' : {
        'bool' :
        {
            'bool' : [True, 'bool'],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'int' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'float' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'char' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'string' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        }
    },
    '|' : {
        'bool' :
        {
            'bool' : [True, 'bool'],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'int' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'float' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'char' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        },
        'string' :
        {
            'bool' : [False],
            'int' : [False],
            'float' : [False],
            'char' : [False],
            'string' : [False]
        }
    }
}