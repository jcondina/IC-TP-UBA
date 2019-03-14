import imfilters
from scipy import misc
import time
import numpy as np

#La siguiente funcion se utiliza para medir los tiempos en los que se ejecuta cada filtro
def medirTiempos(fn, *args):
    t1=time.time()
    fn(*args)
    t2=time.time()
    return float(t2-t1)

#Filtros de python, en ambos casos se aplica a la matriz las cuentas que se explican en el pdf del tp (en C++ se hace lo mismo):
def gray_filter(a):
    R=a[:,:,0]
    G=a[:,:,1]
    B=a[:,:,2]
    newImg=0.3*R+0.6*G+0.11*B
    return newImg  

def blur_filter(a):
    for i in range(1, len(a)-1):
        for j in range(1, len(a[i])-1):
            a[i][j]=(a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1])/4
    return a

#Se carga una imagen como matriz y se la pasa a matriz de numpy (sino la función en C++ no puede usarla como parámetro)
img=misc.imread('imagen.jpg')
img=np.array(img)

#Ejecución de todas las funciones (primero python, despues C++
bnw=(gray_filter(img))
print('Tiempo Gray filter Python:', medirTiempos(gray_filter, img))

blured=(blur_filter(bnw))
misc.imsave('blured.jpg', blured) #Esta funcion guarda la imagen
print('Tiempo Blur filter Python:',medirTiempos(blur_filter, bnw))

imgC=misc.imread('imagen.jpg')
imgC=np.array(imgC)

grayC=imfilters.gray_filter(imgC)
print('Tiempo Gray filter C++:',medirTiempos(imfilters.gray_filter, imgC))

blurC=imfilters.blur_filter(grayC)
misc.imsave('blurC.jpg', blurC)
print('Tiempo Blur filter C++:',medirTiempos(imfilters.blur_filter, grayC))

# utilizar misc.imread(archivo, matriz) para leer imágenes de un archivo
#          misc.imsave(archivo, matriz) para escribir imágenes a un archivo

# COMPLETAR EL RESTO DEL CÓDIGO PEDIDO A CONTINUACIÓN
