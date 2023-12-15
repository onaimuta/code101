import os
import platform
from datetime import datetime
now = datetime.now()
print ("This is "+platform.platform()+" Built on "+os.name+" Technology")
# print ("Your request was fully processed at" +datetime.now())
#print (os.environ)