def f(n):
    if(n < 1):
        return ""
    if(n == 1):
        return "*"
    else:
        string = "*"
        for i in range(n-1):
            string += "/*"
        return string

print(f"f(4) returns \"{f(4)}\"")
print(f"f(1) returns \"{f(1)}\"")