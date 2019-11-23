import socket
import io
from PIL import ImageGrab, Image, ImageDraw
import time

update_time = 3
html = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<meta http-equiv="refresh" content="{}">
<head>
<title>Desktop</title>
</head>
<body>
<image src="/desktop.png" style="background-size: 100% auto;"
</body>
</html>
""".format(update_time)

image_rep = """HTTP/1.0 200 OK
Content-Type: image/png

"""

host, port = "", 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(10)
print("开始监听8000")

while True:
  client, (client_ip, client_port) = server.accept()
  request = client.recv(1024)
  print(request)
  request = str(request, encoding='utf-8')
  print("连接客户端 ip 地址为：", client_ip)
  # time.sleep(2)
  if "GET /desktop.png HTTP/1.1" in request:
    imbuffer = io.BytesIO()
    imdesktop = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    imdesktop.save(imbuffer, 'png')
    imcontents = imbuffer.getvalue()
    imbuffer.close()
    client.sendall(bytes(image_rep, encoding='utf-8') + imcontents)
    time.sleep(20)
  elif 'GET / HTTP/1.1' in request:
    client.sendall(bytes(html, encoding='utf-8'))
  else:
    client.sendall(bytes('HTTP/1.0 404 Not Found\r\n', encoding='utf-8'))
  client.close()


# imbuffer = io.BytesIO()
# print(imbuffer)
# imdesktop = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
# imdesktop.save(imbuffer, 'png')
# # imdesktop.save('a.png')
# imcontents = imbuffer.getvalue()
