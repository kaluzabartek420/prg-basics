ean = input("Enter EAN-13 article number: ")
if(ean.isdigit() and len(ean) == 13):
    print("Article number is correct")
    if(ean[0:3] == "590"):
        print("Article manufactured in Poland")
else:
    print("Article number is incorrect")