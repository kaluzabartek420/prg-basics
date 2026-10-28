def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if(i % 2 == 0 and i % 3 == 0 and i % 4 != 0):
            sum += i
    return sum

print(f"f(1,20) returns {f(1,20)}")
print(f"f(10,30) returns {f(10,30)}")