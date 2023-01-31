import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time
import keyboard
import win32api
from PIL import Image
from mss import mss

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

def ss(cor, resolution=[0]):   
    if resolution[0] ==0:
        a=cor[0]
        b=cor[1]
        c=abs(cor[2]-cor[0])
        d=abs(cor[3]-cor[1])
        mon = {'top': a, 'left':b, 'width':c, 'height':d}
        
        sct = mss()
       #begin_time = time()
        sct_img = sct.grab(mon)
        img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
        img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
       #print('This frame takes {} seconds.'.format(time()-begin_time))
        return img_bgr
    else:
        if resolution ==0:
            a=cor[0]
            b=cor[1]
            c=abs(cor[2]-cor[0])
            d=abs(cor[3]-cor[1])
            mon = {'top': a, 'left':b, 'width':c, 'height':d}
            
            sct = mss()
           #begin_time = time()
            sct_img = sct.grab(mon)
            img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
            img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            img_bgr = cv2.resize(img_bgr, resolution)
           #print('This frame takes {} seconds.'.format(time()-begin_time))
            return img_bgr
        
def capture(area,fps=60):

    
    
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



#ss use usage
#frame=ss([470,440,1320,890])

#capture usage / you need to interrupt with key press "1"
#capture([470,440,1320,890])
