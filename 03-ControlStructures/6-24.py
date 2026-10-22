stars=1

while stars < 5:
    line = ""
    for i in range(stars):
        line += "* "
    print(line)
    stars += 1

while stars > 0:
    line = ""
    for i in range(stars):
        line += "* "
    print(line)
    stars -= 1