import numpy as np
import cv2
import time
import keyboard
import win32api

"""
Resolution Type	Common Name	Aspect Ratio	Pixel Size
SD (Standard Definition)	480p	4:3	640 x 480
HD (High Definition)	720p	16:9	1280 x 720
Full HD (FHD)	1080p	16:9	1920 x 1080
QHD (Quad HD)	1440p	16:9	2560 x 1440
2K video	1080p	1:1.77	2048 x 1080
4K video or Ultra HD (UHD)	4K or 2160p	1:1.9	3840 x 2160
8K video or Full Ultra HD	8K or 4320p	16∶9	7680 x 4320
"""
def ss(cor, resolution=[640,480]):     
    frame = np.array(ImageGrab.grab(bbox=(cor[0],cor[1],cor[2],cor[3])))
    frame = cv2.resize(frame, resolution)
    return frame



#%%

while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break  # finishing the loop

    frame=ss([470,440,1320,890])
    
    #do some action here
    
    
    
#%%

# with 4 fps its almost real time speed but due to low exampling rate its look kinda weard
# this issue bucause i used my cpu if you use your gpu you should fine and ignore that
# to active gpu you need some operation then use this with "tf.device('GPU:0'):" like function then do your action
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

