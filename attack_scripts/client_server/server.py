import socket
s= socket.socket()
host = '0.0.0.0'
port = 1234
s.bind((host,port))
s.listen()
c,addr=s.accept()
print("connected ....",addr)
msg=input('> ')
while msg != 'e':
    if not msg:
        msg=input("> ")
        continue
        
    c.send(msg.encode())
    data = c.recv(1024)
    print(data.decode())
    msg = input("> ")
    
s.close()