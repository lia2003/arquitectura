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

        #Lee el documento y saca lso valores
        with open("notas.csv", "r") as f:
            contenido = f.read()
        
        

        mensaje_client= contenido.encode('utf-8')
        #Envía el mensaje 
        socket_client.sendall(mensaje_client)
        #Una vez enviado espera respuesta del server con el promedio 
         
        mensaje_server = socket_client.recv(CLIENT_BUFFER)
        if(mensaje_server):
            msg_server = mensaje_server.decode('utf-8')
            print(f"El promedio es: {msg_server}") 
            #Imprime el mensaje recibido, se escribe el mensaje por teclado, se codifica, se envía y se sigue el proceso
                    
    except KeyboardInterrupt:
            print("Servidor cerrado manualmente por el usuario...")
    finally:
       socket_client.close()


