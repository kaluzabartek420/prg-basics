def f(number):
    sum = 0
    numberstring = str(number)
    for char in numberstring:
        if(numberstring.count(char) > 1):
            sum += int(char)
    return sum

print(f"f(1027) returns {f(1027)}")
print(f"f(230335) returns {f(230335)}")
print(f"f(513553007) returns {f(513553007)}")