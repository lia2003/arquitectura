import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
SERVER_BUFFER = 1024
N_CLIENTS = 5


if __name__ == '__main__':

    # socket() ---> nos permite crear un objeto de tipo socket
    # AF_INET ---> nos indica que se utilizarán direcciones IPv4
    # SOCK_STREAM ---> nos indica que se utilizará el protocolo TCP

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    # bind() ----> Nos permite asociar una interfaz de red específica a nuestro servidor
    socket_server.bind(server_address)

    # listen() ---> Nos permite habilitar el socket del server para recibir conexiones de clientes
    socket_server.listen(N_CLIENTS)

    print(f"Servidor de tiempo escuchando en {SERVER_HOST}:{SERVER_PORT}")

    while (1):
        # Espera a que un cliente se conecte
        socket_client, client_address = socket_server.accept()
        
        
        print(f"Conexión entrante desde {client_address}")
                
        try:
            hora_actual = time.strftime('%H:%M:%S') #guardamos la hora en la variable hora_actual
            #lo enviamos a una cadena de caracteres usando la codificacion utf-8
            hora= hora_actual.encode('utf-8')

            socket_client.sendall(hora) #enviamos la hora al cliente
                
            if not hora:
                break

        finally:
            socket_client.close() #cierra el socket del cliente
 

   
