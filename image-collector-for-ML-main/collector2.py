import pyautogui, sys    
import pyscreenshot as ImageGrab
import PIL 
import win32api
import time 
import keyboard


def if_pressed(c):
    
    a=win32api.GetKeyState(c)
    b=a
    
    while True:
            
        
        
        a=win32api.GetKeyState(49)
        
        
        time.sleep(0.1)
        
        
        if a == b:
            continue
            time.sleep(0.1)
        elif a!= b:
            a = b
            
            return(1)
        
def if_right():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

    while True:
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)

        if a != state_left:  # Button state changed
            state_left = a
            #print(a)
            """
            if a < 0:
                #print('Left Button Pressed')
            else:
                #print('Left Button Released')
            """

        if b != state_right:  # Button state changed
            state_right = b
            #print(b)
            if b < 0:
                #print('Right Button Pressed')
                time.sleep(0.001)
            else:
                #print('Right Button Released')
                return(1)
        



n=0
counter=0

while True:
        
    
    
    if if_right()==1:
    
        time.sleep(0.1)
    
        
        
        print ("state1")
        
        x1, y1 = pyautogui.position()
        
        time.sleep(0.1)
        
        while True:
            
            if if_right()==1:
                print ("state2")
                x2, y2 = pyautogui.position()
                break
            else:
                continue
        counter=counter+1
        im=ImageGrab.grab(bbox=(x1,y1,x2,y2))
        im.save("D:/Data/Metin2/img" +str(n) +".jpg") 
        time.sleep(0.1)
        n=n+1
        

            
            
        
        
        

        

        
        
