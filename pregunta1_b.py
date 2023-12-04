
import asyncio
import random

async def latencia_SMS():
    tiempo_env= random.randint(10,100)
    tiempo_recep= random.randint(10,100)
    latencia_SMS= tiempo_env+tiempo_recep
    #Notar que es en milisegundos 
    await asyncio.sleep(latencia_SMS/1000)
    print(f"La corrutina de la tecnología SMS tuvo una latencia de {latencia_SMS} ms.")
    #Guardamos en el archivo
    linea=f"{latencia_SMS}\n"
    with open("latencias_sms.csv", "a", encoding="utf-8") as f: 
        f.write(linea) 

async def latencia_3G():
    tiempo_ida= random.randint(100,300)
    tiempo_proc= random.randint(10,100)

    latencia_3G= 2*tiempo_ida+2*tiempo_proc
    #Notar que es en milisegundos 
    await asyncio.sleep(latencia_3G/1000)
    print(f"La corrutina de la tecnología SMS tuvo una latencia de {latencia_3G} ms.")
    linea=f"{latencia_3G}\n"
    with open("latencias_3g.csv", "a", encoding="utf-8") as f: 
        f.write(linea)

async def latencia_Satelital():
    tiempo_propa= random.randint(500,700)
    tiempo_recep= random.randint(10,100)

    latencia_Sate= 2*tiempo_propa+tiempo_recep
    #Notar que es en milisegundos 
    await asyncio.sleep(latencia_Sate/1000)
    print(f"La corrutina de la tecnología SMS tuvo una latencia de {latencia_Sate} ms.")
    linea=f"{latencia_Sate}\n"
    with open("latencias_satelital.csv", "a", encoding="utf-8") as f: 
        f.write(linea)

async def main():
    await asyncio.gather(latencia_SMS(),latencia_3G(),latencia_Satelital())

if __name__ == "__main__":
    asyncio.run(main())