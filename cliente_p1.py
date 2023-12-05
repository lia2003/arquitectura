import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    #Creamos el objeto tipo socket, y configuramos para usa IPv4 y TCP
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)
    
    #Se establece conexión hgacia el servidor
    socket_client.connect(server_address)

    try:
        while True:
            contenido=input("Ingrese el nombre del electrodomestico")
            mensaje_client= contenido.encode('utf-8')
            #Envía el mensaje 
            socket_client.sendall(mensaje_client)

            #Recibimos la respuesta
            mensaje_server = socket_client.recv(CLIENT_BUFFER)
            if(mensaje_server):
                msg_server = mensaje_server.decode('utf-8')
                if msg_server=="1":
                    print("Producto en stock. Pedido procesado")
                else:
                    print("Producto agotado. Pedido no procesado")
    finally:
        socket_client.close()