import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",1999))
client.sendall("bonjour")
data = client.recv(1024)
client.close()
print(repr(data))
