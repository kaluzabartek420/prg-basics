###
# Calculates the arithmetic mean of the numbers entered by user
#
total_sum = 0
amount_of_numbers = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    amount_of_numbers += 1

arithmetic_mean = total_sum / amount_of_numbers

print(f"The total sum of {amount_of_numbers} numbers is: {total_sum}")
print(f"Their arithmetic mean is: {arithmetic_mean}")