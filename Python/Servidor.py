import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(5)
 
print ("Servidor de Chat\n")
 
while True:
        print ("Esperando conexión...")
        sc, addr = s.accept()
        print ("Cliente conectado desde: ", addr)
 
        while True:
                recibido = sc.recv(1024)
                if recibido == "quit":
                        break
                print ("Recibido: ", recibido)
 
                nuestra_respuesta = "Hola cliente, yo soy el servidor. Unete a underc0de!"
                sc.send(nuestra_respuesta.encode('utf-8'))
 
print ("Adios")
sc.close()
s.close()

