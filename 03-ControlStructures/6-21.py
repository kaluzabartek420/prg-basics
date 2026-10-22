amount = int(input("Enter the amount in PLN: "))
amount_remainder = amount

if(amount_remainder / 5 != 0):
    coins_5 = amount_remainder // 5
    amount_remainder = amount_remainder % 5
if(amount_remainder / 2 != 0):
    coins_2 = amount_remainder // 2
    amount_remainder = amount_remainder % 2
if(amount_remainder / 1 != 0):
    coins_1 = amount_remainder // 1
    amount_remainder = amount_remainder % 1

print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")