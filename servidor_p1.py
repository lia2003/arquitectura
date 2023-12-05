import socket
from threading import Thread

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
SERVER_BUFFER = 1024

stock = {"lavadora": 5, "refrigerador": 3,  "aspiradora": 2, "licuadora": 4}


def manejar_al_cliente(client_conn, client_addr):
    try:
        while True:
            mensaje_client = client_conn.recv(SERVER_BUFFER)
            if(mensaje_client):
                msg_client = mensaje_client.decode('utf-8')
                
            #Esto quiere decir si es que el mensaje está en la lista "Su nombre"
            #Y además su cantidad es mayor que 0 envía, si no guarda
            if msg_client in stock and stock[msg_client] > 0:
                stock[msg_client] -= 1
                respuesta = "1"
            else:
                respuesta = "0"
            client_conn.send(respuesta.encode('utf-8'))   
    finally:
        print("El cliente a cerrado la conexión")

if __name__ == '__main__':
    #Creamos el objeto tipo socket, y configuramos para usa IPv4 y TCP
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)
    # Asociamos la interfas a server_address, es decir un puerto y una IP
    socket_server.bind(server_address)
    # Habilitamos la conexión de los clientes, en este caso 1 por vez
    socket_server.listen(1)

    try:    
        while True: 
            client_conn, client_addr = socket_server.accept()
            thread= Thread (target= manejar_al_cliente, args= (client_conn, client_addr))
            thread.start()
    finally:
        socket_server.close()