def f(expression):
    result = int(expression[0])
    for i in range(2,len(expression),2):
        if(expression[i-1] == "+"):
            result += int(expression[i])
        else:
            result -= int(expression[i])
    return result

print(f"f(\"2+3\") returns {f('2+3')}")
print(f"f(\"3+8+1\") returns {f('3+8+1')}")
print(f"f(\"2+3-4+5-0\") returns {f('2+3-4+5-0')}")