###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
radius_1 = 1
radius_2 = 3
pi = math.pi
# calculate area 
area_1 = round(pi * radius_1 ** 2,2)
area_2 = round(pi * radius_2 ** 2,2)
# calculate circumference 
circumference_1 = round(2 * pi * radius_1,2)
circumference_2 = round(2 * pi * radius_2,2)
# print results 
print(f"r = {radius_1} ---> circumference = {circumference_1}, area = {area_1}")
print(f"r = {radius_2} ---> circumference = {circumference_2}, area = {area_2}")