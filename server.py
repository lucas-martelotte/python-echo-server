import socket

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(6)

print('Server started. Listening to connections on port 5000.')

connection, address = server.accept()
while True:
  data = connection.recv(1024)
  if data is None:
      break
  connection.sendall(data)

connection.close()