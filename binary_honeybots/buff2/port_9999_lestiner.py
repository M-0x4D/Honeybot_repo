import socket
import requests
import time


s= socket.socket()
host = '0.0.0.0'
port = 9999

while(True):
    
    try:
        s.bind((host,port))
        s.listen()
        print(f"listening on port {port} ..." )
        # url ==> "http://127.0.0.1:3333/api/system/?format=json"
        url = "http://127.0.0.1:3333/api/system/?format=json"
        myobj = {'honeybot_name': 'binary_vulnserver'}
        res = requests.post(url , data = myobj)
       
    except:
        print("can not lestin on this port")
        time.sleep(2)
        