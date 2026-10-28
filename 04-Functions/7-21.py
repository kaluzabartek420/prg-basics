def f(number1,number2,number3):
    # largest number
    if(number1 >= number2 and number1 >= number3):
        largest = number1
    elif(number2 >= number1 and number2 >= number3):
        largest = number2
    else:
        largest = number3

    # smallest number
    if(number1 <= number2 and number1 <= number3):
        smallest = number1
    elif(number2 <= number1 and number2 <= number3):
        smallest = number2
    else:
        smallest = number3

    return (largest - smallest)

print(f"f(7,4,9) returns {f(7,4,9)}")
print(f"f(2,12,8) returns {f(2,12,8)}")