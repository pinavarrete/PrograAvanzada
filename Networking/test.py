import socket

# Creamos un socket para una conexión TCP con IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10001

# El metodo bind "enlaza" el socket a un puerto dado, en este caso el puerto 80
s.bind((host,port))

# Con el método listen() pedimos al sistema operativo que empiece a escuchar por
# potenciales conexiones al socket. El argumento corresponde al número máximo de
# conexiones pendientes permitidas.
s.listen(5)

cont = 0
while True:
    # Establecemos la conexión
    socket_cliente, address = s.accept()
    print("Obtuvimos una conexión desde %s" % str(address))
    socket_cliente.send("{}. Hola nuevo amigo!\n".format(cont).encode("ascii"))
    info = socket_cliente.recv(1024)
    print(info.decode('ascii'))
    socket_cliente.close()
    cont += 1
