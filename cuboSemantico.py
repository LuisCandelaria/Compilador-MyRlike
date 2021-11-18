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
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "booleano"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "booleano"]
        }
    },
    '>' : {
        "int" :
        { 
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "booleano"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "booleano"]
        }
    },
    '<' : {
        "int" :
        { 
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "booleano"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "booleano"]
        }
    },
    '!=' : {
        "int" :
        { 
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [True, "booleano"], 
            "float" : [True, "booleano"], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True, "booleano"], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True, "booleano"]
        }
    },
    '=' : {
        "int" :
        { 
            "int" : [True], 
            "float" : [False], 
            "char" : [False], 
            "string" : [False]
        },
        "float" :
        {
            "int" : [False], 
            "float" : [True], 
            "char" : [False], 
            "string" : [False]
        },
        "char" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [True], 
            "string" : [False]
        },
        "string" :
        {
            "int" : [False], 
            "float" : [False], 
            "char" : [False], 
            "string" : [True]
        }
    }
}