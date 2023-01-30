import pyautogui
import time
def Click(x,y,right=0,delay=0.5):
    if right==0:        
        pyautogui.moveTo(x, y,delay)
        time.sleep(delay)
        pyautogui.click()
    if right==1:
        
        pyautogui.moveTo(x, y,delay)
        time.sleep(delay)
        pyautogui.click(button='right')