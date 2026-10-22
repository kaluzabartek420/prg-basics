onetothirty = ""
for i in range(1, 31):
    if(i % 3 == 0 and i % 5 == 0):
        onetothirty += "BINGO "
    elif(i % 3 == 0):
        onetothirty += "THREE "
    elif(i % 5 == 0):
        onetothirty += "FIVE "
    else:
        onetothirty += str(i) + " "
print(onetothirty)