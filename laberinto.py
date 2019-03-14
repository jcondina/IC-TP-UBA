# -*- coding: utf-8 -*-    

from copy import deepcopy

class Laberinto(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.posicionRata = (0,0)
        self.posicionQ = (0,0)
        self.laberintos = []
        self.tamanoLab = (0,0)
        self._solucion = []
	
    ##### interfaz (metodos publicos)

    def cargar(self, fn):
        self.laberintos = []
        size = open(fn).readline()
        size = size.replace("Dim", "").replace("(", "").replace(")", "").split(",")
        self.tamanoLab = (int(size[0]), int(size[1]))

        self._crearMatrizSolucion(self.tamanoLab[0], self.tamanoLab[1])

        entrada = open(fn).readlines()
        for linea in entrada[1:]:
                aux = linea.replace('[','').split(']')[:-1]
                for i in range(len(aux)):
                    aux[i] = aux[i].split(',')
                self.laberintos.append(aux)
        self.resetear()
    
    def esPosicionQueso(self, i, j):
        posicion=(i,j)
        if posicion == self.posicionQ:
            return True
        else:
            return False 

    def esPosicionRata(self, i, j):
        posicion = (i,j)
        if posicion == self.posicionRata:
            return True
        else:
            return False
    
    def get(self, i, j):
        celda = []
        for l in range(len(self.laberintos[i][j])):
            if self.laberintos[i][j][l] == '1':
                celda.append(True)
            else:
                celda.append(False)
        return celda
        
    def getInfoCelda(self,i,j):
        return self._solucion[i][j]

    def getPosicionQueso(self):
        return self.posicionQ

    def getPosicionRata(self):
        return self.posicionRata

    def resetear(self):
        self.posicionRata = (0,0)
        self.posicionQ = (self.tamanoLab[0]-1, self.tamanoLab[1]-1)
        self._resetearSolucion(self.tamanoLab[0], self.tamanoLab[1])

    def resolver(self):
        posicionInicial = self.getPosicionRata()
        return self._mover(posicionInicial[0], posicionInicial[1])

    def resuelto(self):
        if self.getPosicionRata() == self.getPosicionQueso():
            return True
        else:
            return False

    def setPosicionQueso(self,i,j):
        self.posicionQ = (i,j)
        if self.laberintos[i][j] == 0:
            return True
        if self.laberintos[i][j] == 1:
            return False

    def setPosicionRata(self, i, j):
        self.posicionRata = (i,j)
        if self.laberintos[i][j] == 0:
            return True
        if self.laberintos[i][j] == 1:
            return False

    def tamano(self):
        return self.tamanoLab

	##### auxiliares (metodos privados)

    def _crearMatrizSolucion (self, i, j):
        diccionario = {'visitada':False, 'caminoActual':False}
        self._solucion = []
        for r in range(i):
            row=[]
            for c in range(j):
                row.append(deepcopy(diccionario))
            self._solucion.append(row)

    def _marcarCeldaCaminoActual(self, i, j, booleano):
        self._solucion[i][j]['caminoActual'] = booleano

    def _marcarCeldaVisitada(self, i, j):
        self._solucion[i][j]['visitada'] = True

    def _mover(self, i, j):
        if (self.resuelto()):
           return True
        if i>=0 and j>=0 and i<self.tamanoLab[0] and j<self.tamanoLab[1] and self._solucion[i][j]['visitada'] == False:
            self.setPosicionRata(i,j)
            self._marcarCeldaVisitada(i,j)
            self._marcarCeldaCaminoActual(i,j, True)
            self._redibujar()
            paredesCelda = self.get(i,j)
            #ir abajo
            if (paredesCelda[3] == False):
                if self._mover(i+1, j):
                    return True
            #ir derecha
            if (paredesCelda[2] == False):
                if self._mover(i, j+1):
                    return True
            #ir arriba
            if (paredesCelda[1] == False):
                if self._mover(i-1, j):
                    return True
            #ir izquierda
            if (paredesCelda[0] == False):
                if self._mover(i, j-1):
                    return True
            #backtracking
            self.setPosicionRata(i,j)
            self._marcarCeldaCaminoActual(i,j, False)
            self._redibujar()
            return False
        return False

    def _redibujar(self):
            if self.parent is not None:
                self.parent.update()

    def _resetearSolucion(self, i, j):
        for r in range(i):
            for c in range(j):
                self._solucion[r][c]['visitada'] = False
                self._solucion[r][c]['caminoActual'] = False