# importing the required packages
import pyautogui
import cv2
import numpy as np
from win32api import GetSystemMetrics 
import socket
import pickle
import imutils
from PIL import ImageGrab
import struct

  

#create socket 
s = socket.socket()
s.connect(('127.0.0.1',8888))

img_counter =0
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

  
while True:
    # Take screenshot using PyAutoGUI
    img = ImageGrab.grab(bbox=None) #x, y, w, h
    #img = pyautogui.screenshot()
   
    frame = np.array(img)
    
    res , image = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(image, 0)
    size = len(data)
    #print(data)
    
    #print(ret)
    # 鏡像
   
    #result, image = cv2.imencode('.jpg', frame, encode_param)
  
    #print(data)
    #print(img_np)
    #res = pickle.dumps(img_np)
    #############frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    #print(frame)
    
    
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
   
    
    
    if img_counter%10==0:
        s.sendall(struct.pack(">L", size) + data)
        
        
  
    # Convert the screenshot to a numpy array
    ###frame = np.array(img)
    #print(frame)
    ###frame_bytes = frame.tobytes()
    ###s.sendall(frame_bytes)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    ###frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
    img_counter += 1
  
    # Write it to the output file
    ###out.write(frame)
      
    # Optional: Display the recording screen
    #cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()