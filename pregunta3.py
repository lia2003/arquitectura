import asyncio

 #Primero definimos los jugadires y sus ratings
jugadores = {
    "Magnus": 2882,
    "Vladimir": 2774,
    "Peter": 2753,
    "Levon": 2767,
    "Boris": 2747,
    "Alexander": 2764
}

#Con ello hacemos una función que nos permita saber cuando un jugador gana, esto es lo
#que se ejecuta de manera asíncrona pues mencionan que las partidas son las que se ejecutan de forma
#Aíncrona

async def partido(jugador1, jugador2):
    rating_jugador1 = jugadores[jugador1]
    rating_jugador2 = jugadores[jugador2]

    #mediante la tupla sacamos los ratings y dependiendo de que puntaje sea mayor retornamos al ganador del encuentro
    if rating_jugador1 > rating_jugador2:
        ganador= jugador1
    else:
        ganador= jugador2
        
    if(ganador=="Magnus"):
        puntajes[0]=puntajes[0]+1
    elif (ganador=="Vladimir"):
        puntajes[1]=puntajes[1]+1
    elif (ganador=="Peter"):
        puntajes[2]=puntajes[2]+1
    elif (ganador=="Levon"):
        puntajes[3]=puntajes[3]+1
    elif (ganador=="Boris"):
        puntajes[4]=puntajes[4]+1
    elif (ganador=="Alexander"):
        puntajes[5]=puntajes[5]+1
    
async def fase_grupos():
    #Aquí se guardarán los puntajes de forma ordenada, es decir, Magnus, Valdimir,...
   

    #También se podría ejecutar las fechas de forma asíncrona pero no lo menciona el enunciado y pregunté al Jefe de Práctica y me dijo
    #que no
    #En la fecha 1:
    await asyncio.gather(partido("Levon", "Magnus"),partido("Boris", "Alexander"),partido("Peter", "Vladimir"))
    #En la fecha 2:
    await asyncio.gather(partido("Magnus", "Vladimir"),partido("Alexander", "Peter"),partido("Levon", "Boris"))
    #En la fecha 3:
    await asyncio.gather(partido("Boris", "Magnus"),partido("Peter", "Levon"),partido("Vladimir", "Alexander"))
    #En la fecha 4:
    await asyncio.gather(partido("Magnus", "Alexander"),partido("Levon", "Vladimir"),partido("Boris", "Peter"))
    #En la fecha 5:
    await asyncio.gather(partido("Peter", "Magnus"),partido("Vladimir", "Boris"),partido("Alexander", "Levon"))

    #Para sacar el valor del mayor 
    mayor=0
    for i in range(1,7):
        if puntajes[i]>mayor:
            mayor=puntajes[i]
            pocision=i
    #Para sacar el ganador:
    if(pocision==0):
        ganador="Magnus"
    elif (pocision==1):
        ganador="Vladimir"
    elif (pocision==2):
        ganador="Peter"
    elif (pocision==3):
        ganador="Levon"
    elif (pocision==4):
        ganador="Boris"
    elif (pocision==5):
        ganador="Alexander"
    print(f"El ganador es {ganador}")

if __name__ == "__main__":
    puntajes=[0,0,0,0,0,0]
    asyncio.run(fase_grupos())
    
