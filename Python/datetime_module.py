from datetime import datetime
from calendar import Calendar
#from tzlocal import get_localzone
from pytz import timezone
format =  "%d-%m-%Y %H:%M:%S %Z%z"
now_utc = datetime.now(timezone("CAT"))
print (now_cat.strftime(format))