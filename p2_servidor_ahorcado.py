import random
import socket

my_IP = "127.0.0.1"
port = 5000

#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]



if __name__ == "__main__":
    #crear socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar (unir) el socket al host y puerto
    server_socket.bind((my_IP, port))

    # Escucha hasta 5 conexiones entrantes
    server_socket.listen(5)

    print(f"Servidor de ahorcado escuchando en {my_IP}:{port}")

    while True:
        # Espera a que un cliente se conecte
        client_socket, client_address = server_socket.accept()
        print(f"Conexión entrante desde {client_address}")

        cmd = client_socket.recv(1024)  # Recibe datos del cliente. Como maximo 1024 bytes
        #decodificar
        #el servidor solo recibira 2 cosas, start y las letras a adivinar
        #por lo tanto asumiremos que primero recibira el start y dsps las palabras

        if cmd.decode('utf-8')== 'start':
            print(f"Recibí comando {cmd.decode('utf-8')}")
        else:
            #debemos escoger una palabra random de la lista dictionary
            palabra= random.choice(dictionary)
            #enviamos la palabra elegida
            client_socket.send(palabra.encode('utf-8'))
            
            print(f"Palabra elegida: {palabra}")
            #debe imprimir las palabras enviadas por el cliente
            #inicializamos la cantidad de letras recibidas
            i=0
            adivinanza= cmd.decode('utf-8')
            while(i<=4): #solo podemos recibir 5 adivinanzas
                print(f"Client guess: {adivinanza}")
                client_socket.send(adivinanza.encode('utf-8'))
                #actualizamos adivinanza
                adivinanza = client_socket.recv(1024).decode('utf-8')
                i= i+1
                if (i==5):
                    print("Closing conection")
                    #cerramos la conexion con el cliente
        
        if not cmd:
            break
