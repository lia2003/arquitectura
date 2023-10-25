import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    # socket() ---> nos permite crear un objeto de tipo socket
    # AF_INET ---> nos indica que se utilizarán direcciones IPv4
    # SOCK_STREAM ---> nos indica que se utilizará el protocolo TCP

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    # connect() ---> nos permite enviar una solicitud de conexión hacia el servidor
    socket_client.connect(server_address)

    # TX
 
    msg_TX = "Hola server! :D"
    # encode('utf-8') ---> Nos permite enviar la información en formato de B
    data_TX = msg_TX.encode('utf-8')
    socket_client.sendall(data_TX)

    # RX
    data_RX = socket_client.recv(CLIENT_BUFFER)
    print(f"{data_RX.decode('utf-8')}")

    print("Cliente cerrando la conexión...")
    socket_client.close()