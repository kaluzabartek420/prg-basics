def time_string(hours, minutes, time_format):
    if(time_format == "12"):
        if(hours < 12):
            prefix = "am"
        else:
            prefix = "pm"
        hours_formatted = hours % 12
        if(hours_formatted == 0):
            hours_formatted = 12
    else:
        prefix = ""
        hours_formatted = hours
    
    if(minutes < 10):
        minutes_string = "0" + str(minutes)
    else:
        minutes_string = str(minutes)
    
    return(f"{hours_formatted}:{minutes_string}{prefix}")

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))