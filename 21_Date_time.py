# OBJECTIVE: write a python program to print daate and time

# from datetime import datetime
# today= datetime.today()
# print("Today's date is", today)




# write a python progarm add some days to current day and print it
import datetime
from datetime import timedelta

today=datetime.date(2023, 2,3)
print(today)

enddate=today+ timedelta(days=7)
print(enddate)