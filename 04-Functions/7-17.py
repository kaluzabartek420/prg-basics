def f(palindrome):
    reversed = ""
    for char in palindrome:
        reversed = char + reversed
    if(palindrome == reversed):
        return True
    else:
        return False

print(f"f(\"radar\") returns {f('radar')}")
print(f"f(\"12-11-21\") returns {f('12-11-21')}")
print(f"f(\"book\") returns {f('book')}")