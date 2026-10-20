parking_hours = int(input("Enter parking hours: "))
if(parking_hours <= 2):
    parking_fee = 5
elif(parking_hours <= 6):
    parking_fee = 10
else:
    parking_fee = 20
print(f"Parking fee: {parking_fee} PLN")