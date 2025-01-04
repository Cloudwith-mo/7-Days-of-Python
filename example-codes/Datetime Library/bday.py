from datetime import datetime, timedelta

# Get current date & time
now = datetime.now()
print(now) 

# Create a datetime for a specific date & time
date = datetime(2025, 5, 1, 12, 0)
print(date)

#Calculate the difference between two dates
delta = now - date
print(delta)

