def lettercounter(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    return counter