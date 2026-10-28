def sum_natural(n):
    if(n==1):
        return n
    else:
        return (n + sum_natural(n-1))

print(f"sum_natural(10) returns {sum_natural(10)}")