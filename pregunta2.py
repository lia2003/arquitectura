from threading import Thread
from urllib.request import urlopen
import time
#Parte a, donde las imágenes se descargan de forma secuencial
def descargar_secuencial():

    for i in range(1,30):
        if (i<=9):
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/0{i}.png"
        else:
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i}.png"

        with urlopen(url) as page:#accede a la url
            image_data = page.read() #se descarga la imagen
            with open(f"imagen{i}.jpg", 'wb') as destino:#coloca la imagen en el archivo imagen{i}
                destino.write(image_data)
#Ahora descargamos los archivos utilizando hilos

def descargar_imagen(i):
    if (i<=9):
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/0{i}.png"
    else:
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i}.png"
    with urlopen(url) as page:
        image_data = page.read() 
        with open(f"imagen{i}.jpg", 'wb') as destino:
            destino.write(image_data)

#Aquí es la parte b), deonde descarga 1 imagen en cada hilo
def descargar_con_hilos_cada_uno():   
    hilos = []
    for i in range(1, 30):
        hilo = Thread(target=descargar_imagen, args=(i,))
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()
#Aquí es la parte c) donde descarga usando 3 hilos

def descargar_tres_hilos():
    
    #Así es como se consigue, primero, como hay 3 hilos se le asignará una imagen a cada
    #Uno, por eso salta de 3 en 3
    for i in range(1, 30, 3): 
        #Una vez ya se tiene el intervalo de 3, los 3 hilos que tenemos debem
        #Encargarse de descargar esas tres imagenes, una cada uno
        hilos = [] #Lista para guardar los 3 hilos
        for j in range(3):
            #Luego, se debe considerar j+i porque no tendría sentido
            #de solo ser j, pues se descargaría una imagen que ya se 
            #descargó anmteriormente
            if i + j <= 29:  
                #Asímismo, como en mi código i representa
                #el número de imagen, nos aseguramos que no
                #sean mayor al establecido que es 29
                hilo = Thread(target=descargar_imagen, args=(i + j,))
                hilos.append(hilo)
                hilo.start()
        #Para asegurarnos que el programa principal no acabe hasta que todos los hilos lo hayan hecho
        for hilo in hilos:
            hilo.join()


if __name__ == '__main__':
    tic1 = time.perf_counter()
    descargar_secuencial()
    toc1 = time.perf_counter()
    descargar_con_hilos_cada_uno()
    tic2 = time.perf_counter()
    descargar_tres_hilos()
    toc2=time.perf_counter()
    tiempo_1=toc1-tic1
    tiempo_2=tic2-toc1
    tiempo_3=toc2-tic2

    print(tiempo_1,tiempo_2,tiempo_3)

    #Con respecto a la implementación de la función descargar_con_hilos_cada_uno donde
    #se descarga con un hilo por cada imagen, puedo mencionar que el tiempo me resulta
    #inferior, eso sería la comparación entre t1 y t2, ello se debe a que al descargarse
    #las 29 imágenes concurrentemente se ahorra tiempo, pues mientras se descarga una, la 
    #Otra empieza, diferente a la forma secuencial, donde para descargar una imagen se debe
    #de esperar a que se complete la descarga de la anterior. Ello al momento de ejectur se 
    #Ya que resulta aproximadamente 1,93 para el tiempo secuencial y 0,35 para el tiempo en 
    # el que se usan 29 hilos.


    #Con respecto a la implementación de la función 3, se esperaría que el tiempo que le toma a 
    #descargar_tres_hilos sea superior respecto al tiempo que le tomó a la función descargar_con_
    #hilos_cada_uno, ello se debe a que si bien aprovechamos 3 hilos, en cada hilo se está dando un 
    #Proceso secuencial donde se descargan un cierto número de imágenes. Ello al momento de ejectur se 
    #Ya que resulta aproximadamente 0,34 para el tiempo de 29 hilos y 0,89 para el de 3.

