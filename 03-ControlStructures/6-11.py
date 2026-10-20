current_price = 140.00
previous_price = 200.00
percent_decreased = (1 - (current_price / previous_price)) * 100
if(percent_decreased >= 10):
    print(f"Buy the product!!")
    print(f"Product price reduced by {int(percent_decreased)}%")