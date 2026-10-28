def f(name):
    acronym = name[0]
    for i in range(len(name)):
        if(name[i] == " "):
            acronym += name[i+1]
    return acronym

print(f"f(\"Internet of Things\") returns \"{f('Internet of Things')}\"")
print(f"f(\"For Your Information\") returns \"{f('For Your Information')}\"")
print(f"f(\"Python\") returns \"{f('Python')}\"")