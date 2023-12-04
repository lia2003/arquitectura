import aiofiles
import asyncio
import random
import time

#Primero que todo pienso que la razón principal por la que se ejecuta más lento es porque en sí no se está
#ganando una mejora específica en este código, por ejemplo si en cada función la durmieramos un tiempo aproximado
#Es decir que espere un cierto tiempo para finalmente crear el archivo el tiempo de ejecución sería mucho más notorio
#Que hay una ventaja respecto a su forma sincrona, diferente a lo que ocurre donde los tiempos son tan pequeños que 
#tarda más en ejecutar las funciones de la misma libreria asyncio que de forma asíncrona, en otros casos como por ejemplo
#en el que mencioné suponiendo que tuviera que esperar cada función 2 segundos será evidente que en este caso sí habrá
#Una diferencia notable 


#Otra razón puede ser la limitada cantidad de funciones que se ejecutan, que al ser tan pocas no se afecta de forma significativa en
#La suma de tiempos de forma síncrona Pues de ser una gran cantidad el tiempo que suma sí repercutiría de forma,
#Notable en que los tiempos de forma asíncrona sean menores.  En este caso para suponer eso ejecutaremos las 
#funciones no 3 veces si no 10 veces cada una de forma sincrona y asíncrona. 

#Notar que presento 2 docuementos, el segundo es para la forma síncrona y este en el que realizo las modificaciones de forma asíncrona

#La primera modificación será que las funciones esperen un cierto tiempo, 1 segundo por ejemplo, para la parte sincrna usé time 

#Así con estas modificaciones notamos que la diferencia es extremadamente grandes, pues aproximadamente se notará una diferencia de 30 segundos
#Causa de estas 2 modificaciones 

#Cabe recalcar que como ya vimos el uso de asincronismo no siempre nos garantiza mejoras en la ejecución, de ello podemos rescatar que esta 
#Es una herramienta útil dependiendo de las situaciones en las que se use, por ejemplo de ser usada para códigos en los que 
#Se ejecuten cientos o miles de funciones o en códigos que tengan funciones con lapsos mucho mayores de ejecución, tal y como
#se demostró.

async def genera_labs():
    codigo_inicial = 20230001
    await asyncio.sleep(1)#Modificación
    async with aiofiles.open("notas_labs.csv", "w+") as f:
        cabecera = "codigo,"
        cabecera += ",".join([f"lab_{i}" for i in range(1, 15)])
        cabecera += "\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},"
            linea += ",".join([f"{random.randint(0, 20)}" for i in range(1, 15)])
            linea += "\n"
            await f.write(linea)


async def genera_parcial():
    codigo_inicial = 20230001
    await asyncio.sleep(1)#Modificación
    async with aiofiles.open("notas_parcial.csv", "w+") as f:
        cabecera = "codigo,parcial\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def genera_final():
    codigo_inicial = 20230001
    
    await asyncio.sleep(1)#Modificación
    async with aiofiles.open("notas_final.csv", "w+") as f:
        cabecera = "codigo,final\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def main():
    #Modificación
    await asyncio.gather(genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final(),genera_labs(), genera_parcial(), genera_final())


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")