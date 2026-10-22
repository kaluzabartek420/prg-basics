n = int(input("Enter a number of leading prime numbers: "))
found = 0
number = 2
numbers = ""

while(found != n):
    factors = 0
    for i in range (1, number+1):
        if(number % i == 0):
            factors += 1
    if(factors == 2):
        found += 1
        numbers += str(number) + " "
    number += 1

print(f"Prime numbers: {numbers}")