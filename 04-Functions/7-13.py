def f(n):
    string = ""
    for i in range(1, n+1):
        string += str(i)
    return string

print(f"f(11) returns \"{f(11)}\"")
print(f"f(4) returns \"{f(4)}\"")