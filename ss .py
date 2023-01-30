import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time
import keyboard

def ss(cor):     
    frame = np. array(ImageGrab. grab(bbox=(cor[0],cor[1],cor[2],cor[3]))) 
    return frame



while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break  # finishing the loop

    frame=ss([470,440,1320,890])
    
    #do some action here
    
    
    
