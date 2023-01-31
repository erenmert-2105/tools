import win32api


a=win32api.GetKeyState(49)
b=a
while True:
    a=win32api.GetKeyState(49)
    #break if press 1
    if a!= b:
        break