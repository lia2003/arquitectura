import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    # socket() ---> nos permite crear un objeto de tipo socket
    # AF_INET ---> nos indica que se utilizarán direcciones IPv4
    # SOCK_STREAM ---> nos indica que se utilizará el protocolo TCP

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT) #direccion del server
    
    #conectar al servidor
    socket_client.connect(server_address)
        

    while True:
        # Enviar el mensaje
        message = input("Cliente: ")
        socket_client.send(message.encode('utf-8')) #envia los datos al servidor
        data = socket_client.recv(CLIENT_BUFFER) #recibe datos del servidor
        dataDeco = data.decode('utf-8')
        print(f"Servidor: {dataDeco}")
        if message == 'exit':
            socket_client.send(message.encode('utf-8')) #enviamos el exit
            break #y le damos a break el bucle



