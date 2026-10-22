decimal = int(input("Enter decimal number: "))
decimal_remainder = decimal
binary = ""
while(decimal_remainder > 0):
    binary = str(decimal_remainder % 2) + binary
    decimal_remainder = decimal_remainder // 2
print(f"{decimal}(10) = {binary}(2)")