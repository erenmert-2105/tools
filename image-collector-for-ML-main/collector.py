import pyscreenshot as ImageGrab
import PIL 
import win32api
import time 



n=0
counter=0
a=win32api.GetKeyState(49)
b=a
while True:
        
    
    
    a=win32api.GetKeyState(49)
    
    print(a)
    time.sleep(0.1)
    
    
    if a == b:
        continue
        time.sleep(0.1)
    elif a!= b:
        a = b
        print ("happend")
        
        counter=counter+1
        
        
        # fullscreen
        

#(1745,590,1835,680)2
#(1535,590,1625,680)3
        # part of the screen
        im=ImageGrab.grab(bbox=(1745,590,1835,680))
        
        #im.show()

        im.save("img" +str(n) +".jpg") 
        time.sleep(0.1)
        n=n+1
        
        if b ==1:
            b=0
        elif b==0:
            b=1
        