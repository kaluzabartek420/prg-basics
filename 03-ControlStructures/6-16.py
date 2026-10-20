washing_product = "shoes"
rinse = True
spin = False

washing_time = 0
if washing_product == "jacket":
    washing_time += 40
if washing_product == "underwear":
    washing_time += 70
if washing_product == "shoes":
    washing_time += 20
if rinse:
    washing_time += 15
if spin:
    washing_time += 9

print(f"Total washing time: {washing_time} minutes")