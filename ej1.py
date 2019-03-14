import math
import sys
import random
import time

#La lista de puntos puede ser importada como archivos externo con la funcion listaDePuntos(fn),
#siempre y cuando se respete el formado que se muestra en el archivo'numeros' incluido con los ejercicios
def listaDePuntos(fn):
    l=[]
    entrada=open(fn)
    for linea in entrada:
        tupla = (float(linea.split(" ")[0]), float(linea.split(" ")[1]))
        l.append(tupla)
    return l

#Si quiere generarse una lista de puntos al azar, utilizar directamente la función
#generarPuntos(n), donde n es la cantidad de tuplas que quieran generarse
   
def generarPuntos(n):
    a=[]
    i=n
    while i>0:
        generarPunto=random.random(), random.random()
        a.append(generarPunto)
        i-=1
    return a


def distanciaMinima(a):
    distancias=[]
    distMin=1000
    for i in range(len(a)):
        count=i+1
        while count<len(a):
            n=math.sqrt(((a[i][0]-a[count][0])**2+(a[i][1]-a[count][1])**2))
            distancias.append(n)
            if n<distMin:
                distMin=n
                puntos=[a[i],a[count]]
            count+=1
    return puntos, distMin

#a=listaDePuntos(sys.argv[1])
a=listaDePuntos("numeros")
#print(distanciaMinima(a))
print(a)
	
def maxPos(a, b, c):
    i=b
    pos=0
    while i<c:
        if a[i][0]>pos:
            pos=i
        i+=1
    return pos
        
    
def upSort(a):
    elemento=len(a)-1
    n=0
    while elemento>0:
        n=maxPos(a, 0, elemento)
        a[n], a[elemento]=a[elemento], a[n]
        elemento=elemento-1
    return a

print(upSort(a))
    
def mergeSort(a):
    if len(a)>1:
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k]=lefthalf[i]
                i=i+1
            else:
                a[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            a[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            a[k]=righthalf[j]
            j=j+1
            k=k+1
    return a

def python(a):
    a.sort()
    return a

def distancia(a,b):
    return math.sqrt(((a[0]-b[0])**2+(a[1]-b[1])**2))
        
def distanciaMinimaDyC(a, algoritmo):
    dMin=1000
    b=algoritmo(a)
    if len(b)==3:
        dBase=distancia(b[0],b[1])
        dBase2=distancia(b[1],b[2])
        dBase3=distancia(b[0],b[2])
        if dBase<dBase2 and dBase<dBase3 and dBase<dMin:
            dMin=dBase
        if dBase2<dBase and dBase2<dBase3 and dBase2<dMin:
            dMin=dBase2
        if dBase3<dBase and dBase3<dBase2 and dBase3<dMin:
            dMin=dBase3
    if len(b)>2:
        mid = len(b)//2
        lefthalf = b[:mid]
        righthalf = b[mid:]
        i=0
        distanciaMinimaDyC(lefthalf, algoritmo)
        distanciaMinimaDyC(righthalf, algoritmo)
       
        while i<len(lefthalf):
            d1=distancia(b[i],b[i+1])
            if d1<dMin:
                dMin=d1
            i+=1
        while i<len(righthalf):
            d2=distancia(b[i],b[i+1])
            if d2<dMin:
                dMin=d2
            i+=1
        d3=distancia(lefthalf[-1], righthalf[0])
        if d3<dMin:
            dMin=d3
    return dMin


b=generarPuntos(15)

print(b)
print(distanciaMinimaDyC(a, mergeSort))
print(distanciaMinima(b))
print(distanciaMinimaDyC(b, mergeSort))




