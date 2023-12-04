import socket
import numpy as np

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
SERVER_BUFFER = 1024
N_CLIENTS = 1

if __name__ == '__main__':
      
    #Creamos el objeto tipo socket, y configuramos para usa IPv4 y TCP
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)

    # Asociamos la interfas a server_address, es decir un puerto y una IP
    socket_server.bind(server_address)

    # Habilitamos la conexión de los clientes, en este caso 1 por vez
    socket_server.listen(N_CLIENTS)

    print(f"Servidor de tiempo escuchando en {server_address[0]}:{server_address[1]}")

    while (1):
        #Establecemos la conexión
        client_conn, client_addr = socket_server.accept()
        try:  
            #En esta iterativa se reciben los mensajes del server, se decodifican y se imprimen
            while(1):
                #Recibe en bytes
                mensaje_client = client_conn.recv(SERVER_BUFFER)
                if(mensaje_client):
                    #Lo decodifica a str
                    msg_client = mensaje_client.decode('utf-8')
                    c_lista = msg_client.split(",")
                    #Luego de esto ya tiene las notas del alumno en un arreglo, como sabemos el número exacto
                    #Podemos dividirlo el listas específicas:
                    nota_practica=[c_lista[0],c_lista[1],c_lista[2],c_lista[3]]
                    nota_practica_i=[int(elemento) for elemento in nota_practica]
                    nota_labs=[c_lista[4],c_lista[5],c_lista[6],c_lista[7],c_lista[8],c_lista[9],c_lista[10],c_lista[11],c_lista[12],c_lista[13]]
                    nota_labs_i=[int(elemento) for elemento in nota_labs]
                    nota_TA_i=int(c_lista[14])
                    #Luego procedemos a calcular lo necesitado
                    #Promedio de labs:
                    for i in range(1,3):
                        menor_valor=np.min(nota_labs_i)
                        nota_labs_i.remove(menor_valor)
                    #Lo hace 2 veces pues sacamos el valor 2 veces, luego scamos promedio
                    promedio_labs_i=np.mean(nota_labs_i)
                    
                    #Promedio pcs
                    menor_valor_p_i=np.min(nota_practica_i)
                    nota_practica_i.remove(menor_valor_p_i)
                    #Lo hace 2 veces pues sacamos el valor 2 veces, luego scamos promedio
                    promedio_pcs_i=np.mean(nota_practica_i)

                    #Promedio total:

                    prom=((3*promedio_pcs_i)+(3*promedio_labs_i)+(4*nota_TA_i))/10
                    msg_server=f"{prom}"
                    #Luego de haber respondido se codifica a bytes y se envía para seguir con el ciclo
                    #hasta que el cliente mande exit
                    mensaje_server= msg_server.encode('utf-8')
                    client_conn.sendall(mensaje_server)

        except KeyboardInterrupt:
            print("Servidor cerrado manualmente por el usuario...")
            break
        finally:
            client_conn.close()