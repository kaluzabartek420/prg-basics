import random

random_numbers = ""

for i in range(20):
    random_number = random.randint(5, 10)
    random_numbers += str(random_number) + " "

print(random_numbers)