import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time
import keyboard

def ss(cor):     
    frame = np. array(ImageGrab. grab(bbox=(cor[0],cor[1],cor[2],cor[3]))) 
    return frame


frame=ss([470,440,1320,890])


#%%

while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break  # finishing the loop

    frame=ss([470,440,1320,890])
    
    #do some action here
    
    
    
#%%

# with 4 fps its almost real time speed but due to low exampling rate its look kinda weard
area=[470,440,1320,890]
fps=4

screenshots = []
a=win32api.GetKeyState(49)
b=a
while True:
    a=win32api.GetKeyState(49)
    if a!= b:
        break
    # Get the screenshot
    screenshot = ss(area)
    # Append it to the list of screenshots
    screenshots.append(screenshot)

    

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
size = screenshots[0].shape[1::-1]
video = cv2.VideoWriter('output.mp4', fourcc, fps, size)

# Write each frame to the video
for frame in screenshots:
    video.write(frame)

# Release the video writer
video.release()

