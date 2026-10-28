def f(binary_number):
    for char in binary_number:
        if(char != "0" and char != "1"):
            return False
    return True

print(f"f(\"101101\") returns {f('101101')}")
print(f"f(\"1311a10100\") returns {f('1311a10100')}")