###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = round(fuel_consumption / 100 * distance, 2)
total_cost = round(total_fuel_consumption * fuel_price, 2)
print(f"Total fuel consumption in liters: {total_fuel_consumption}")
print(f"Total cost of transporting goods: {total_cost}")
