from xyrangefunction import inrange

number = 7
start = 2
end = 15

if(inrange(7,2,15)):
    suffix = "yes"
else:
    suffix = "no"

print(f"A number: {number}")
print(f"Number {number} in the range <{start},{end}>: {suffix}")