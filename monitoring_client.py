import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_1_PORT = 50000
SERVER_2_PORT = 50001
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    # socket() ---> nos permite crear un objeto de tipo socket
    # AF_INET ---> nos indica que se utilizarán direcciones IPv4
    # SOCK_STREAM ---> nos indica que se utilizará el protocolo TCP
    while(1):

        try:  
            socket_client_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address_1 = (SERVER_HOST, SERVER_1_PORT) #asocia la direccion del server 1

            socket_client_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address_2 = (SERVER_HOST, SERVER_2_PORT) #asocia la direccion del server 2

            # connect() ---> nos permite enviar una solicitud de conexión hacia el servidor
            socket_client_1.connect(server_address_1) #se conecta al server 1
            socket_client_2.connect(server_address_2) #se conecta al server 2
            
            # RX
            data_estado_1 = socket_client_1.recv(CLIENT_BUFFER) #recibe los datos del server 1
            data_estado_2 = socket_client_2.recv(CLIENT_BUFFER) #recibe los datos del server 2
            datos_1=data_estado_1.decode('utf-8').split(',') #decodifica los datos del server1
            datos_2=data_estado_2.decode('utf-8').split(',') #decodifica los datos del server2

            #imprime los datos
            if data_estado_1 and data_estado_2:
                print(f"Información de uso del servidor {SERVER_HOST}:{SERVER_1_PORT}: CPU Usage: {datos_1[0]}, RAM Usage: {datos_1[1]}")
                print(f"Información de uso del servidor {SERVER_HOST}:{SERVER_2_PORT}: CPU Usage: {datos_2[0]}, RAM Usage: {datos_1[1]}")
            #cada 5 segundos
            time.sleep(5)           
                       
        
        finally:
            socket_client_1.close()
            socket_client_1.close()

        