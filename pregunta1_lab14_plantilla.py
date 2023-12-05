import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 20 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

#Parte a) En esta seccón se resuelve la pregunta de forma asíncrona
def retornar_correcta():
	valor=0
	vocales=['a','e','i','o','u']
	for v_1 in vocales:
		for v_2 in vocales:
			for v_3 in abecedario:
				clave= v_1+v_2+v_3
				valor=comparar_con_password_correcto(clave)
				if valor:
					correcta=clave
					break
			if valor:
				break
		if valor:
			break	
	print(correcta)
#Parte b) En esta sección se va a resolver con multiprocessing
#Vocal por vocal la primera iteración puedo tomarla como un multiproceso
#Es decir, por cada proceso asumir una vocal, para ello definimos la función 
#Con función de entrada una vocal

def retornar_correcta_vocal(vocal):
	valor=0
	for v_2 in vocales:
		for v_3 in abecedario:
			clave= vocal+v_2+v_3
			valor=comparar_con_password_correcto(clave)
			if valor:
				correcta=clave
				break
		if valor:
			break
	return clave

def retornar_multiprocess():
    correcta = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    with Pool(processes=5) as p:
        resultados = p.map(retornar_correcta_vocal, vocales)
    for valor in resultados:
        if valor:  
            correcta = valor
            break
    print(correcta)


if __name__ == "__main__":
	t1=time.perf_counter()
	retornar_correcta()
	t2=time.perf_counter()
	retornar_multiprocess()
	t3=time.perf_counter()
	print(f"Tiempo de ejecución síncrono: {t2-t1}")
	print(f"Tiempo de ejecución asíncrono: {t3-t2}")
