
class ArbolBinario:
    def __init__(self):
        self.raiz= None
        self.izq= None
        self.der= None
    
    def raiz(self):
        return self.raiz
#    si esta vacio? 
        
    def vacio(self):
        if self.raiz == None:
            return True 
        else: 
            return False 
#        si no tiene raiz puede tener ramas? para mi no.. si la respuesta
#            fuera si...habría que agregar los ifs para las ramas.. 
#    es decir...no alzanzaría solo con que self.raiz sea None
            
        
    def bin(self, a, izq, der):
        self.raiz = a 
        self.izq = izq
        self.der = der
        return str(self.raiz)
        
    def izquierda(self):
        return self.izq
    
    def derecha(self):
        return self.der
        
    def find(self, a):
        if a== self.raiz:
            return True
        if self.izq != None:
            return self.izq.find(a)
        if self.der != None:
            return self.der.find(a)
        return False
            
    def espejo(self): 
        self.bin (self.raiz,self.der,self.izq)
        if self.izq != None:
            self.izq.espejo()
        if self.der != None:
            self.der.espejo()
        
x= bin(5,2,1)
print(x)
#    def inserta(self, nuevo):
#        if nuevo== self.elto:
#            return self
#        elif nuevo< self.elto:
#            if self.izdo== None:
#                self.izdo= Arbol(nuevo)
#            else:
#                self.izdo= self.izdo.inserta(nuevo)
#        else:
#            if self.dcho== None:
#                self.dcho= Arbol(nuevo)
#            else:
#                self.dcho= self.dcho.inserta(nuevo)
#        return self
    


