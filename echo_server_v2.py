import socket

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

    print(f"Inicializando servidor con dirección {server_address[0]} y puerto {server_address[1]}")

    while (1):
        print("Servidor esperando conexiones clientes...")

        # accept() ---> Nos permite establecer la comunicación entre cliente-servidor
        client_conn, client_addr = socket_server.accept()

        try:
            print(f"Conexión establecida con cliente con dirección {client_addr[0]} y puerto {client_addr[1]}")

            while(1):
                data_RX = client_conn.recv(SERVER_BUFFER) 

                if data_RX:
                    # decode('utf-8') ---> Nos permite enviar la información en formato de B
                    msg_RX = data_RX.decode('utf-8')
                    print(msg_RX)
                    client_conn.sendall(data_RX)
                else:
                    break

        # except KeyboardInterrupt:
        #     print("Servidor cerrado manualmente por el usuario...")

        finally:
            print("El cliente ha finalizado la conexión...")
            #socket_server.close()
