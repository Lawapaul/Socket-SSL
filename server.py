import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',65431))
server_socket.listen(1)

conn, addr = server_socket.accept()

sbox = {
    "1001" : "Harshit",
    "1002" : "Singh"
}
input = conn.recv(1024).decode()
result = sbox.get(input,"Invalid String")

conn.send(result.encode())
server_socket.close()
