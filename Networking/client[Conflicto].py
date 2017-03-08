import socket

# Creamos un socket para una conexión TCP con IPv4
s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos el nombre de la máquina local
host = socket.gethostname()
port = 10001
s_cliente.connect((host,port))
data = s_cliente.recv(1024)
print(data.decode('ascii'))
s_cliente.close() 