###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Enter a SWIFT code: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
# BPKOPLPW: Bank Code: BPKO; Country Code: PL
# CHASUS33: Bank Code: CHAS; Country Code: US
# DEUTDEFF: Bank Code: DEUT; Country Code: DE