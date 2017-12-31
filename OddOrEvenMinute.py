from datetime import datetime

right_this_minute = datetime.today().minute

if right_this_minute%2==1:
    print("This minute is odd")
else:
    print("Not an odd minute")
