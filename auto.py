import pywhatkit 
import time

ph='+91 8304831623'
base_msg="Ooi"

for i in range(1,1001):
    msg=f"{i} {base_msg}"
    try:
        pywhatkit.sendwhatmsg(ph,msg, 12,47)
        print(f"message sent: {msg}")
    except Exception as e:
        print()

