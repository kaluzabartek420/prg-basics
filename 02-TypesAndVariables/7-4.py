import math
circumference = int(input('Enter tree circumference in cm: '))
diameter = circumference / math.pi
can_be_cut_down = diameter >= 50
print(f'Tree can be cut down: {can_be_cut_down}')
# Drzewa 1 (d = 160 cm) i 3 (d = 230 cm) mogą zostać ścięte