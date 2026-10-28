def f(sentence):
    nospacesentence = ""
    for char in sentence:
        if char != " ":
            nospacesentence += char
    return nospacesentence

print(f"f(\"integrated development environment\") returns \"{f('integrated development environment')}\"")
print(f"f(\"A programming language is a system of notation for writing computer programs\") returns \"{f('A programming language is a system of notation for writing computer programs')}\"")