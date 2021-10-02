# sin hijos
    def __init__(self,name):
        self.name = name
    
    def imprimir(self,ident):
        print(ident+"Entero: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[Entero = "+str(self.name)+"]"+"\n"
        
        return id



# con un hijo
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"

        return id



# con dos hijos
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        return id



# con tres hijos
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        return id



# con cuatro hijos
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        txt += id + "->" + son4 + "\n"
        return id



# con cinco hijos
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
    
    def imprimir(self, ident):
        #if str(type(self.son1)) == "<type 'tuple'>":
        #elif str(type(self.son1)) == "<type 'instance'>":
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" " + ident)
        else:
            self.son5.imprimir(" " + ident)
        
        print(ident + "Nodo: " + self.name)
    
    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        
        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        
        txt += id + "[label = "+self.name+"]"+"\n"
        txt += id + "->" + son1 + "\n"
        txt += id + "->" + son2 + "\n"
        txt += id + "->" + son3 + "\n"
        txt += id + "->" + son4 + "\n"
        txt += id + "->" + son5 + "\n"
        return id