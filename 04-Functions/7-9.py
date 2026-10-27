def f(number,even):
    numberstring = str(number)
    sumeven = 0
    sumodd = 0
    for char in numberstring:
        n = int(char)
        if(n % 2 == 0):
            sumeven += n
        else:
            sumodd += n
    if(even):
        return sumeven
    else:
        return sumodd

print("f(3124,True) returns",f(3124,True))
print("f(3124,False) returns",f(3124,False))
print("f(20576,False) returns",f(20576,False))
print("f(20576,True) returns",f(20576,True))
print("f(13115,True) returns",f(13115,True))