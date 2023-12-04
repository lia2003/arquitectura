import random
import time

#Comentario en la Parte "sync"

def genera_labs():
    codigo_inicial = 20230001
    time.sleep(1)#Modificación
    with open("notas_labs.csv", "w+") as f:
        cabecera = "codigo,"
        cabecera += ",".join([f"lab_{i}" for i in range(1, 15)])
        cabecera += "\n"
        f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},"
            linea += ",".join([f"{random.randint(0, 20)}" for i in range(1, 15)])
            linea += "\n"
            f.write(linea)


def genera_parcial():
    codigo_inicial = 20230001
    time.sleep(1)#Modificación
    with open("notas_parcial.csv", "w+") as f:
        cabecera = "codigo,parcial\n"
        f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            f.write(linea)


def genera_final():
    codigo_inicial = 20230001
    time.sleep(1)#Modificación
    with open("notas_final.csv", "w+") as f:
        cabecera = "codigo,final\n"
        f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            f.write(linea)


def main():#Modificación
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()
    genera_labs()
    genera_parcial()
    genera_final()

if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")