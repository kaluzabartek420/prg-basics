number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))
if(number_of_products <= 2):
    total_price = product_price * number_of_products
else:
    total_price = (2 * product_price) + ((number_of_products - 2) * (0.75 * product_price))
print(f"Amount to pay: {round(total_price, 2)}")