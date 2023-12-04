
import random
import asyncio
import matplotlib.pyplot as plt
import time
import aiofiles


#Parte a, donde se generan los M archivos de N caracteres
# cada uno, en una subcarpeta denominada “original”. Para ello,
# solo debe cambiar el nombre de su archivo a “./original/archivo1”.
# Pruebe su funcion con M = 3 y N = 1024. (1 pt)
def generar_archivos(M, N):
    for i in range(1,M+1):
        # Crea M archivos 
        linea = ""
        for j in range(1,N+1):
            linea += f"{random.randint(1, 9)},"
        #Sirve para eliminar la coma final
        linea = linea[:-1]

        with open(f"./original/archivo{i}", "w+", encoding="utf-8") as f:
            f.write(linea)

#Parte b, donde se realiza de manera sincrona
# función que copie los archivos de la carpeta “original” a una
# carpeta llamada “copia” de manera síncrona. Solo utilice las funciones
# nativas de python.
def sincronica(M):
    for i in range(1, M + 1):
         with open(f"./original/archivo{i}", 'rb') as origen:
            contenido =  origen.read()
         with open(f"./copia/archivo{i}", 'wb') as destino:
            destino.write(contenido)


#Parte c, donde se realiza de manera asíncrona
async def copiar(i): 
    
    async with aiofiles.open(f"./original/archivo{i}", 'rb') as origen:
        contenido = await origen.read()
    async with aiofiles.open(f"./copia/archivo{i}", 'wb') as destino:
        await destino.write(contenido)

async def main(M):
    await asyncio.gather(*[copiar(i) for i in range(1, M + 1)])

def asincronica(M):
    asyncio.run(main(M))
#Aquí se implementan las partes donde se varía M y N y se obtienen las gráficas

def variando_N(M):

    lista_N = [2**i for i in range(10,26)]
    tiempos_sync = []
    tiempos_async = []

    for N in lista_N:
        generar_archivos(M,N)

        tic1 = time.perf_counter()
        asincronica(M)
        toc1 = time.perf_counter()
        sincronica(M)
        tic2 = time.perf_counter()
        
        tiempos_sync.append(tic2-toc1)
        tiempos_async.append(toc1-tic1)

    plt.plot(lista_N,tiempos_sync)
    plt.plot(lista_N,tiempos_async)
    plt.xlabel('File size [bytes]')
    plt.ylabel('Copy time [ms]')
    plt.legend(['Sync','Async'])
    plt.savefig('SizeVsTime.png')
    plt.cla()

def variando_M(N):

    lista_M = [2,3,4,5,6,7,8,9,10]
    tiempos_sync = []
    tiempos_async = []

    for M in lista_M:
        generar_archivos(M,N)

        tic1 = time.perf_counter()
        asincronica(M)
        toc1 = time.perf_counter()
        sincronica(M)
        tic2 = time.perf_counter()
        
        tiempos_sync.append(tic2-toc1)
        tiempos_async.append(toc1-tic1)

    plt.plot(lista_N,tiempos_sync)
    plt.plot(lista_N,tiempos_async)
    plt.xlabel('File size [bytes]')
    plt.ylabel('Copy time [ms]')
    plt.legend(['Sync','Async'])
    plt.savefig('SizeVsTime.png')
    plt.cla()


if __name__ == '__main__':
    #Prueba de la función generar_archivos
    M=2
    N=1024
    generar_archivos(2,1024)
    asincronica(2)
    M=3
    variando_N(M)
    N=2**20
    variando_M(N)