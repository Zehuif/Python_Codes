import socket
 
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("192.168.137.1", 8000))
 
while True:
    mensaje = str(input(">> "))
    
    socket_cliente.send(mensaje.encode('utf-8'))  

    recibido = socket_cliente.recv(1024)
    print("Recibido: ", recibido.decode('utf-8'))
 


