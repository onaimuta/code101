
from datetime import date
from datetime import datetime
import pytz

today = date.today()
print("Today's date is:", today)

# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Africa/Kampala'))

# printing current time in india
print("The current time in Uganda is :", current_time)