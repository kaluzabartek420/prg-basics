###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Read Celsius from the keyboard
celsius = float(input("Enter temperature in degrees Celsius: "))
# Calculate Fahrenheit and Kelvin
fahrenheit = (celsius * 9/5) + 32.00
kelvin = celsius + 273.15
# Display the temperature in all units
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")