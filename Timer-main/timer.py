import datetime





now1 = datetime.datetime.now()

def Passed(now1):
    
    now2 = datetime.datetime.now()
    passed = (now2-now1)
    sec = passed.total_seconds()/60
    return sec

if Passed(now1) >= 14:
    print("ended")
    
    


