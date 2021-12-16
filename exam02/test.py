#%%
import sys
from datetime import datetime
import time
import platform

print(sys.version)
print(platform.uname())
# %%
now = datetime.now()
print("now =", now)
print("now time =" + now.strftime("%H%M"))
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"date and time = {dt_string}")	
# %%

print(now.timetuple())
#time stamp   변환 
print(time.mktime(now.timetuple()))
# %%
