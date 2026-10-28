def f(n):
    # number == 2 in first iteration, because 2 is the first
    # natural number greater by 1, so start checking from it
    number = 1
    primecounter = 0
    while(primecounter != n):
        number += 1
        dividers = 0
        for i in range (1, number+1):
            if(number % i == 0):
                dividers += 1
        if(dividers == 2):
            primecounter += 1
    return number

print(f"f(1) returns {f(1)}")
print(f"f(5) returns {f(5)}")