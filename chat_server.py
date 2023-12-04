import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
SERVER_BUFFER = 1024
N_CLIENTS = 10


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

    print(f"Servidor de chat escuchando en {SERVER_HOST}:{SERVER_PORT}")
    while (1): #este bucle acepta varias conexiones del cliente
        #acepta la conexion del cliente
        socket_client, client_address = socket_server.accept()
        print(f"Conexión entrante desde {client_address}") #ya estan conectados
        
        while(1): #dentro de este bucle, se reciben los datos una y otra vez
            data = socket_client.recv(SERVER_BUFFER)  # Recibe datos del cliente. Como maximo 1024 bytes
            dataDeco = data.decode('utf-8')
            if dataDeco == 'exit':
                print(f"Cliente: {dataDeco}")
                seguir=0
                break

            print(f"Cliente: {dataDeco}") #imprime datos enviados por el cliente

            message = input("Servidor: ")
            
            # Envia los el mensaje al cliente
            socket_client.send(message.encode('utf-8')) 
        if seguir==0:
            break



