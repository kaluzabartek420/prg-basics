def f(number1, number2, operator):
    if(operator == "+"):
        return number1 + number2
    elif(operator == "-"):
        return number1 - number2
    elif(operator == "*"):
        return number1 * number2
    elif(operator == "%"):
        return number1 % number2
    elif(operator == "**"):
        return number1 ** number2
    else:
        return 0

print(f"f(2,3, \"+\") returns {f(2,3, '+')}")
print(f"f(2,3, \"%\") returns {f(2,3, '%')}")
print(f"f(2,3, \"**\") returns {f(2,3, '**')}")
print(f"f(2,3, \"*\") returns {f(2,3, '*')}")
print(f"f(2,3, \"-\") returns {f(2,3, '-')}")