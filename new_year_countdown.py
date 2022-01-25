from datetime import *
from time import *
today=datetime.now()
#print(today)
new_year = "2023-01-01-00:00:00"
new_year = datetime.strptime(new_year,"%Y-%m-%d-%H:%M:%S")
#print(new_year)
remaining_time=new_year-today
while(new_year>today):
    print("Time to new year : ",remaining_time, end='\r')
    today=datetime.now()
    remaining_time=new_year-today
    sleep(1)
print("Happy New Year!")

