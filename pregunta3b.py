import random
from multiprocessing import cpu_count, Pool

n=10_000_000

def verfificar_dentro(cuadrante,x,y):
    valor=0
    if cuadrante==1:
        condicion_x= 0<y<(1-(x**2))**(1/2)
        condicion_y= 0<x<(1-(y**2))**(1/2)
    elif cuadrante==2:
        condicion_x= 0<y<(1-(x**2))**(1/2)
        condicion_y= -(1-(x**2))**(1/2)<x<0
    elif cuadrante==3:
        condicion_x= -(1-(x**2))**(1/2)<y<0
        condicion_y= -(1-(y**2))**(1/2)<x<0
    elif cuadrante==4:
        condicion_x= -(1-(x**2))**(1/2)<y<0
        condicion_y= 0<x<(1-(y**2))**(1/2)
    
    if condicion_x and condicion_y:
        valor=1
    return valor

def calcular_pi_areas(cuadrante):
    contador=0
    valor=n/4
    #Para saber si un punto está detro de los valores rqueridos
    #Debemos considerar la forma de una circunferencia
    #1=x^2+y^2
    if cuadrante==1:
        x_sup=1
        x_inf=0
        y_sup=1
        y_inf=0
    elif cuadrante==2:
        x_sup=0
        x_inf=-1
        y_sup=1
        y_inf=0
    elif cuadrante==3:
        x_sup=0
        x_inf=-1
        y_sup=0
        y_inf=-1
    elif cuadrante==4:
        x_sup=1
        x_inf=0
        y_sup=0
        y_inf=-1

    for _ in range(int(n/4)):
        valor=0
        x=random.uniform(x_inf,x_sup)
        y=random.uniform(y_inf,y_sup)
        valor=verfificar_dentro(cuadrante,x,y)
        if valor:
            contador+=1
    return contador


if __name__ == "__main__":

    areas=[1,2,3,4]
    proc = 4

    with Pool(processes=proc) as p:
        resultado = p.map(calcular_pi_areas, areas)
    total_puntos_dentro=sum(resultado)
    Pi=(total_puntos_dentro/n)*4
    print(Pi)