#SEMANA 10 CLASE 1
#1. escritura_codigos.py: Crear y escribir dentro de un archivo
#2. lectura_completa.py: Lee (f.read) e imprime el contenido de un archivo
#3. lectura_parcial.py: Lee (f.readline) e imprime el contenido de un archivo

#SEMANA 10 CLASE 2
#1. echo_client.py: 
# SOCKETS: cliente manda mensaje a servidor 
# y recibe mensaje de servidor
#2. echo_server.py:
# SOCKETS: Servidor recibe mensaje y manda de
# vuelta al cliente

#SEMANA 11 CLASE 1
#1.file_server.py:
# SOCKETS: Servidor busca dentro de un archivo un numero en la posicion 8
# para lo cual crea un archivo con split, que hace el cambio de linea

#SEMANA 11 CLASE 2 PARTE 1
#1. generador_notas.py:
# SOCKETS: Genera 200 codigos, cada uno simula 16 notas,y al final las
# separa en la linea de contenido, y las escribe un archivo notas.csv
# linea[:-1]: utiliza [:-1] para excluir el ultimo caracter de la cadena
# que en este caso es "," y la remplaza con "\n"

#SEMANA 11 CLASE 2 PARTE 2
# 1. notas_client.py: envia el codigo de alumno al server y este responde
# con las notas concatenadas, luego el cliente separa cada nota y 
# saca nota para los laboratorios, ex1 y ex2.

# 2. notas_server.py: ARREGLOS Y POSICIONES
# se envian y reciben datos

#----nota----
# for i in range (4)
# itera de 0 a 3
# for _ in range (4)
# itera de a 0 a 3, se usa cuando no es necesario el uso de la variable
# de iteracion
# for i in range(0, 10, 2):
# itera de 2 en 2 de 0 a 9



# SEMANA 12 CLASE 1 
#1. io_sim_async.py:
# asyncio.gather() para ejecutar las tres funciones asincronicas
# (func1(), func2(), func3()) simultaneamente.
# La funcion asincrona es mas rapida que la sincrona. mitad de tiempo

# SEMANA 12 CLASE 2 PARTE 1
# FUNCION ASINCRONA:
# ------ TEORIA:
# Las funciones asincronas son aquellas que siguen con las 
# demas tareas mientras espera que la operacion i/o se complete
#------- NOTAS:
# async def count():
# await asyncio.sleep(0.1)
# await asyncio.gather(*tasks)
# se usa el *tasks para que cada tarea en la lista sea tratada 
# como un argumento separado para asyncio.gather.
#------- CODIGO:
# generador_notas_sync.py:
# funcion genera_labs:
#codigo,lab_1,lab_2,lab_3,lab_4,lab_5,lab_6,lab_7,lab_8,lab_9...
#20230001,6,17,8,0,12,18,2,10,3,9,12,9,13,2
#20230002,13,12,1,8,3,12,11,6,7,15,10,7,8,13
# funcion genera_parcial:
#codigo,parcial
#20230001,9
#20230002,17
# funcion genera_final:
#codigo,final
#20230001,1
#20230002,14


# SEMANA 12 CLASE 2 PARTE 2
# FUNCION ASINCRONA
# AIOFILES

# SEMANA 13 CLASE 1 PARTE 1
#THREADS
#------- TEORIA
# se usa para que se realice multiples tareas simultaneamente.
#------- DIFERENCIA ENTRE THREADS Y ASYNC:
# THREADS: Guardan el mismo espacio de memoria
# ASYNC: No guardan el mismo espacio de memoria
# Los hilos estan mas relacionados con la ejecucion concurrente
# de codigo en paralelo utilizando multiples hilos de ejecucion,
# mientras que la programacion asincrona se centra en la 
# eficiencia y la no bloqueacion (esperar) al manejar tareas de 
# entrada/salida

# SEMANA 13 CLASE 1 PARTE 2
# SOCKETS Y THREADS

# SEMANA 13 CLASE 2
# SOCKETS Y THREADS
# THREAD POOL
#------ TEORIA
# Se utiliza un ThreadPoolExecutor para ejecutar las tareas 
# concurrentemente. La cantidad de workers sera la cantidad
# de hilos que se creen, se ejecutaran simultaneamente.

# SEMANA 14 CLASE 1
# THREADS y threadpool
# 1.contador_multithreaded_prom.py: se hace una lista de tiempos
# y se saca un promedio de los tiempos medidos
# ------ EJECUCION
# El contador multithreading es mas rapido que el contador sincrono
# ------ TEORIA
# LOCK se utiliza para evitar los race conditions, bloqueas
# una variable para que cuando quieran acceder a ella los
# hilos concurrentes, no se genere una confusion
# un hilo espera a que salga del bloque de lock para poder
# acceder a la funcion y continuar con su ejecucion

# SEMANA 14 CLASE 2 PARTE 1
# REQUESTS/ URLS
# 1. image_download_sync.py: Se descargan imagenes a partir de
# las urls que se dan

# SEMANA 14 CLASE 2 PARTE 2
# MULTIPROCESING
#------ DIFERENCIA ENTRE HILOS Y MULTIPROCESS
# Hilos:Comparten el mismo espacio de memoria y recursos
# Procesos: No comparten memoria directamente
# ----- DIFERENCIA ENTRE MULTIPROCESS Y ASYNC 
# multiprocessing utiliza multiples procesos y puede aprovechar
# multiples nucleos de CPU para ejecutar tareas en paralelo.
# asyncio utiliza un solo hilo y se centra en la concurrencia,
# permitiendo que un programa realice operaciones I/O en paralelo 
# mientras espera de manera eficiente.

# SEMANA 15 CLASE 1 
#"//" division entera
# MULTIPROCESSING

# SEMANA 15 CLASE 2
# multiprocess import pool
# ITERTOOLS
# matriz
# MAP
# La función map aplica una función dada a cada elemento de un 
# iterable (por ejemplo, una lista) en paralelo.
# STARMAP
# La función starmap es similar a map, pero permite pasar 
# múltiples argumentos a la función objetivo.