time_24h = input("Enter time (24-hour format): ")
hours_24h = int(time_24h[0:2])
minutes = int(time_24h[3:5])
if(hours_24h < 12):
    prefix = "am"
    hours_12h = hours_24h
else:
    prefix = "pm"
    hours_12h = hours_24h - 12
if hours_12h == 0:
    hours_12h = 12
time_12h = str(hours_12h) + ":" + str(minutes) + prefix
print(f"Time in 12-hour format: {time_12h}")