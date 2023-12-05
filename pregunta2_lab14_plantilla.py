import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool


def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load('Imágenes en formato npy/'+filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas
    histograma=[0]*256
    histograma = [0] * 256

    for i in range(M):
        for j in range(N):
            histograma[imagen[i][j]] += 1
    return histograma

def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

#PARTE a), calcular el histograma

def calcular_sincrona(imagenes):
    t1=time.perf_counter()
    histogramas=[]
    for imagen in imagenes:
        valor=calcular_histograma(imagen+".npy")
        histogramas.append(valor)
        graficar_histograma(valor, imagen+" sincrono", "black")
    t2=time.perf_counter()
    return t2-t1
#PARTE b), calcular asíncrona

def calcular_asincrona(imagenes, imagenes_2):
    num_proc = 4
    t1 = time.perf_counter()
    
    with Pool(processes=num_proc) as pool:
        resultados = pool.map(calcular_histograma, imagenes_2)

    for imagen, valor in zip(imagenes, resultados):
        graficar_histograma(valor, imagen + "asincrono", "blue")

    t2 = time.perf_counter()
    return t2 - t1

if __name__ == '__main__':

    #Lo que pasa es que para facilitar la implementación de acuerdo a mis funciones
    #Hice que tengan de argumentos o bien una lista o 2 dependiendo, en la síncrona
    #basta con la sita de imágenes con solo los nombres pero en la 2 necesito una 
    #en terminación .npy, no es lo más factible pero sirve para el propósito pues 
    #no tuve tiempo :(
    imagenes_1=['goldhill_x2','hong kong_x2','lena_x2','stonehenge_x2']
    imagenes_2 = ['goldhill_x2.npy', 'hong kong_x2.npy', 'lena_x2.npy', 'stonehenge_x2.npy']

    imagenes_3=['goldhill','hong kong','lena','stonehenge']
    imagenes_4 = ['goldhill.npy', 'hong kong.npy', 'lena.npy', 'stonehenge.npy']

    t_1=calcular_sincrona(imagenes_1)
    print(f"Tiempo total en serie: {t_1}")
    t_2=calcular_asincrona(imagenes_1,imagenes_2)
    print(f'Tiempo de ejecucion en paralelo:{t_2}')
    speed_up_1=t_1/t_2
    print(f"El primer speedup es {speed_up_1}")
    #RESPUESTA A LA PREGUNTA:
    #El speed up de una prueba que obtuve fue de 1,394, lo que implica que si hubo una
    #mejora de aproximadaente un 39 a 40 porciento de la versión asíncrona respecto a la síncrona
    t_3=calcular_sincrona(imagenes_3)
    print(f"Tiempo total en serie: {t_3}")
    t_4=calcular_asincrona(imagenes_3,imagenes_4)
    print(f'Tiempo de ejecucion en paralelo: {t_4}')
    speed_up_2=t_3/t_4
    print(f"El segundo speedup es: {speed_up_2}")
    #El segundo speed up me salio aproximadamente 0,68, lo que implica
    #que hubo una perdida en el rendimiento de aproximadamente 32 porciento
    #La perdida de rendiento puede deberse a que en valores muy pequeños se
    #desperdicia rendimiento al usar muchos procesos que podría facilmente darse 
    #en uno, como los procesos también consumen rendimiento del CPU, ello puede llegar
    #a ser perjudicial

