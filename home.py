import socket
import time
sohum=socket.socket()
print("Socket created")
sohum.bind(('192.168.1.15',9999))
sohum.listen(3)
print("Waiting For Connection")
while True:
    c,address=sohum.accept()
    print("Connect with",address)
    c.send(bytes("Hi this Sohum Server Passcode ref=4843","utf-8"))
    print(c.recv(1024).decode())
    time.sleep(5000)
