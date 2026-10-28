def f(text):
    dashedtext = ""
    for char in text:
        dashedtext += (char + "-")
    if(len(dashedtext) > 0):
        dashedtext = dashedtext[:-1]
    return dashedtext

print(f"f(\"University\") returns \"{f('University')}\"")
print(f"f(\"UE\") returns \"{f('UE')}\"")
print(f"f(\"x\") returns \"{f('x')}\"")
print(f"f(\"\") returns \"{f('')}\"")