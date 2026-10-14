###
# A program that prints your height both in cm and in feet and inches.
#
cm = 185
feet = int(cm // 30.48)
inches = int((cm % 30.48) // 2.54)
# calculate the number of feet

print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches')