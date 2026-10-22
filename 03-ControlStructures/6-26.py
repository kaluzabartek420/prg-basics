pin = "0805"
attempts = 0

while(attempts < 3):
    entered_pin = input("Enter the PIN code: ")
    attempts += 1
    if(entered_pin == pin):
        print("PIN correct.")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")