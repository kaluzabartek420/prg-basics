###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')

# Month 12 is in quarter 4
# Month 10 is in quarter 4
# Month 9 is in quarter 3
# Month 1 is in quarter 1