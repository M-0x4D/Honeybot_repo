
# importing tkinter for gui
import tkinter as tk
from ctypes import *
import pythoncom 
 
 


# creating window
window = tk.Tk()

#gui = tk.Tk(className='Python Examples - Window Color')
# set window size
#gui.geometry("400x200")

#set window color
#gui.configure(bg='blue')
  
# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='black')
window.title("Geeks For Geeks")


  
# creating text label to display on window screen
label = tk.Label(window, text="""
░█░█░█▀█░█▀▀░█░█░█▀▀░█▀▄
░█▀█░█▀█░█░░░█▀▄░█▀▀░█░█
 ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░ 
                            
                             
 
0𝔁4𝓓 𝓲𝓼 𝓗𝓮𝓻𝓮 
               
""" , fg='white' , bg = 'black',width=10000 , height=10000 ,  font=("Arial", 50))
label.pack()
  
window.mainloop()



print("""
███████  ██████  ██████   ██████  ██ ██    ██ ███████     ███    ███ ███████     ███████ ██     ██ ██ ██       █████  ███    ███ 
██      ██    ██ ██   ██ ██       ██ ██    ██ ██          ████  ████ ██          ██      ██     ██ ██ ██      ██   ██ ████  ████ 
█████   ██    ██ ██████  ██   ███ ██ ██    ██ █████       ██ ████ ██ █████       ███████ ██  █  ██ ██ ██      ███████ ██ ████ ██ 
██      ██    ██ ██   ██ ██    ██ ██  ██  ██  ██          ██  ██  ██ ██               ██ ██ ███ ██ ██ ██      ██   ██ ██  ██  ██ 
██       ██████  ██   ██  ██████  ██   ████   ███████     ██      ██ ███████     ███████  ███ ███  ██ ███████ ██   ██ ██      ██ 
                                                                                                                                 """) 
#while True: windll.user32.BlockInput(True)