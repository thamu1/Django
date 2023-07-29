import os
from datetime import datetime

logpath = r"C:\Users\ThamotharanC\OneDrive - Softcrylic LLC\Desktop\Django\csv_mysql\log.txt"



if not os.path.exists(logpath):
    file = open(logpath,'a')
    print("exists")
else:
    file = open(logpath,'a')
    file.write(f"{datetime.now()} fuck you")
    print("created")
    
