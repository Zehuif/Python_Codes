import socket

def conectar():
    global socket_cliente
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect(("192.168.137.1", 8000))
    print('Conectado')
    
def enviar():
    mns='0'
    socket_cliente.send(mns.encode('utf-8'))
    return True

def recibir():
    global recibido
    recibido = socket_cliente.recv(1024)
    recibido=recibido.decode('utf-8')
    print (recibido)
    return True

conectar()
recibir()
enviar()
