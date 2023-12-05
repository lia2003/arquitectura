
import time
from concurrent.futures import ThreadPoolExecutor
import statistics
import requests
urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.python.org/",
    "https://www.reddit.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.cnn.com/",
    "https://www.github.com/",
    "https://www.spotify.com/",
    ]

#Parte a:
#obtenemos
def obtener_y_guardar():
    tic=time.perf_counter()
    i=1
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:#respuesta exitosa
            with open(f"pagina{i}.html", "w", encoding="utf-8") as file:
                file.write(response.text)
        else:
            print("Hubo un error")
        i+=1
    toc=time.perf_counter()
    return (toc-tic)
#Medimos los tiempos 

def medir_tiempo_secuencial():
    tiempos=[]
    for _ in range(5):
        tiempo=obtener_y_guardar()
        tiempos.append(tiempo)
    mediana=statistics.median(tiempos)
    return mediana
#Parte b:

#Creamos la funcion para el Pool

def descargar(url,i):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"pagina{i}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
    else:
        print("Hubo un error")

#Luego descargamos en la función 
def guardar_usando_Thread_Pool(n):
    workers = n
    tic = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        i=1
        for url in urls:
            executor.submit(descargar, url,i)
            i+=1
    toc = time.perf_counter()
    return (toc-tic)
#Medimos los tiempos con Thread
def medir_tiempo_Thread(n):
    tiempos=[]
    for _ in range(5):
        tiempo=guardar_usando_Thread_Pool(n)
        tiempos.append(tiempo)
    mediana=statistics.median(tiempos)
    return mediana

#En esta parte realizaré las prubas con  más workers 


if __name__ == '__main__':
    obtener_y_guardar()
    tiempo_1=medir_tiempo_secuencial()
    guardar_usando_Thread_Pool(3)
    tiempo_2=medir_tiempo_Thread(3)
    print(tiempo_1 , tiempo_2)
    speedup=tiempo_1/tiempo_2
    print("Speedup: ", speedup)
    #En esta parte realizaré las prubas con  más workers
    t_3=medir_tiempo_Thread(10)
    t_4=medir_tiempo_Thread(100)
    print(t_3,t_4)