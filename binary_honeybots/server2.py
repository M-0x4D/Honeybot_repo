import os
import socket
import sys
import psycopg2
from datetime import date
import requests
# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

port = 1000



def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:

            print('Bye')

            # lock released on exit
            print_lock.release()
            break


        # reverse the given string from client
        data = data[::-1]

        # send back reversed string to client
        c.send(data)

        # form = hacker_data(hacker_ip=data,attack_port = port , honeybot_name='system')
        # form.save()

        # connect to postgresql and give it host ip
        # conn = psycopg2.connect(
        #     host="localhost",
        #     database="MHN_DATABASE",
        #     user="postgres",
        #     password="user" )
        #
        # conn.autocommit = True
        #
        # cursorr = conn.cursor()
        #
        # print("connected >>>>")
        # honeybot_name = "system"
        #
        # sql = f"""INSERT INTO 'MHN_REAL_hacker_data'(hacker_ip,attack_port,honeybot_name) VALUES({data} , {port},{honeybot_name});"""
        #
        # cursorr.execute(f"""INSERT INTO MHN_REAL_hacker_data(hacker_ip,attack_port,honeybot_name) VALUES({data} , {port} , {honeybot_name});""")
        # # vendor_id = cur.fetchone()[0]
        # conn.commit()
        # cursorr.close()

    # connection closed
    # c.close()


def Maza_():
    
    host = "127.0.0.1"

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()
        url = 'http://127.0.0.1:8000/remote/api/?format=json'
        obj = {'client_ip':str(addr[0]),'honeybot_name':str(sys.argv[0])}
        x=requests.post(url,data=obj)
        print(x.status_code)

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        
        

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
        
        
Maza_()