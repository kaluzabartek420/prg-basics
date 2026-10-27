def f(amount_to_pay):
    coins = 0

    # 5 PLN coins
    coins += (amount_to_pay // 5)
    amount_to_pay = (amount_to_pay % 5)
    # 2 PLN coins
    coins += (amount_to_pay // 2)
    amount_to_pay = (amount_to_pay % 2)
    # 1 PLN coins
    coins += amount_to_pay
    amount_to_pay = 0

    return coins

print("f(23) returns", f(23))
print("f(8) returns", f(8))
print("f(2) returns", f(2))
print("f(0) returns", f(0))