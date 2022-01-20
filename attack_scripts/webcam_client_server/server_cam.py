import socket
import cv2
import sys
import matplotlib.pyplot as plt
import pickle
import numpy as np
import struct ## new
import zlib
from PIL import Image, ImageOps
from win32api import GetSystemMetrics 

s= socket.socket()
host = '0.0.0.0'
port = 6666
s.bind((host,port))
s.listen()
c,addr=s.accept()
print("connected ....",addr)
######################################3
# Specify video codec
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

  
# Specify name of Output file
filename = "Record.mp4"
  
# Specify frames rate. We can choose any 
# value and experiment with it
fps = 5.0
  
width = 640
height = 480

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, fourcc, fps, (width,height))

i = 0
data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        data += c.recv(4096)
    # receive image row data form client socket
    packed_msg_size = data[:payload_size]  #from fisrt to 5
    data = data[payload_size:]  # from 5 to end
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += c.recv(4096)
    frame_size = data[:msg_size]
    data = data[msg_size:]
    # unpack image using pickle 
    frame=pickle.loads(frame_size, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    
    out.write(frame)
    cv2.imshow('server',frame)
    # Save Frame by Frame into disk using imwrite method
    #cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    #i += 1
    
    

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()