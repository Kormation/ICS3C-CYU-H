# Programmer: 
# Description: 

num_days = 0

months = [
    "January", 
    "February", 
    "March", 
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#num_days = [31,28,31,30,31,30,31,31,30,31,30,31]

month = input("Please enter the month : ")
month = month.title()

while month not in months:
    print("Invalid month! Try again.")
    month = input("Please enter the month : ")
    month = month.title()
    
if month in ["January", "March", "May", "July", "August", "October", "December"]:
    num_days += 31
    print(f"{month} has {num_days} days")

elif month in ["April", "June", "September", "November"]:
    num_days += 30
    print(f"{month} has {num_days} days")
    
else:
    print("February has 28 or 29 days")
    
