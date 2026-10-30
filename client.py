import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',65431))

string = input("Enter String: ")
client_socket.send(string.encode())

result = client_socket.recv(1024).decode()
print(result)

client_socket.close()