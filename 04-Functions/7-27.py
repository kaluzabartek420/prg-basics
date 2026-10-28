def f(product_code):
    firstthree = product_code[:3]
    sumfirstthree = 0
    for char in firstthree:
        sumfirstthree += int(char)
    if((sumfirstthree % 7) == int(product_code[3])):
        return True
    return False

print(f"f(\"1082\") returns {f('1082')}")
print(f"f(\"2035\") returns {f('2035')}")
print(f"f(\"1114\") returns {f('1114')}")
print(f"f(\"7071\") returns {f('7071')}")