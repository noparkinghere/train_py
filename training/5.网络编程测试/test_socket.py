from socket import *

myhost = ''
myport = 8082
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(128)
while True:
  connection, address = sockobj.accept()
  print("connect by")
  print(address)
  while True:
    data = connection.recv(1024)
    if not data:
      break
    connection.send("echo".encode('utf-8')+data)
  connection.close()