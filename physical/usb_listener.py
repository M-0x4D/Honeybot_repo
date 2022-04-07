import win32file
import requests
import time
import pyfiglet

class check_usb:

    
    
    def locate_usb():
        drive_list = []
        run_once = 0
        drivebits = win32file.GetLogicalDrives()
        for d in range(1, 26):
            mask = 1 << d
            if drivebits & mask:
                # here if the drive is at least there
                drname = '%c:\\' % chr(ord('A') + d)
                t = win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
                    if run_once == 0:
                        check_usb.send_server(drive_list)
                        run_once = 1
                    else:
                        pass
                    
        return drive_list
      

    def send_server(connected_device):
        
        url = "http://127.0.0.1:3333/api/system/?format=json"
        body = {"honeybot_name" : connected_device , 
                "port" : "usb_port"}
        res = requests.post(url , data = body )
        
        
        
        
  
if __name__ == "__main__":
    result = pyfiglet.figlet_format("USB LISTENER")
    print(result)
    while(True):
        
        check_usb.locate_usb()
        time.sleep(5)
    
    
#import win32api
#import win32file


#while(True):
#    try:
#        
#        # Returns a list containing letters from removable drives
#        drive_list = win32api.GetLogicalDriveStrings()
#        drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
#        for letter in drive_list:
#            if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:# check if the drive is of type removable 
#                print("list drives: {0}".format(letter))
#    except:
#        pass