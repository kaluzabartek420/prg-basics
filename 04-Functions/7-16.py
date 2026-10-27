def f(n):
    a = 0
    b = 1
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return b

print(f"f(5) returns {f(5)}")
print(f"f(9) returns {f(9)}")