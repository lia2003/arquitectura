import socket
import psutil

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 50001
SERVER_BUFFER = 1024
N_CLIENTS = 1


if __name__ == '__main__':

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)
    socket_server.bind(server_address)
    socket_server.listen(N_CLIENTS)

    print(f"Servidor de monitoreo escuchando en {server_address}:{server_address}")

    while (1):
        #aceptamos la conexion del cliente
        client_conn, client_addr = socket_server.accept()
        try:  
            cpu_percent = psutil.cpu_percent(interval=0)#saca el % de cpu usado
            mem_info = psutil.virtual_memory().percent #saca el % de ram usado

            info_str= f"{cpu_percent},{mem_info}" #saca estos valores en un string
            
            message=info_str.encode('utf-8') #los codifica
            client_conn.sendall(message)  #los manda               
                       
        finally:
            client_conn.close() #finaliza la conexion con el cliente