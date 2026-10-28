def f(dice):
    diceroll = dice[0]
    inarow = 1
    maxdiceroll = diceroll
    maxinarow = inarow

    for i in range(1,len(dice)):
        if(dice[i] == diceroll):
            inarow += 1
        else:
            diceroll = dice[i]
            inarow = 1

        if(inarow > maxinarow):
            maxdiceroll = diceroll
            maxinarow = inarow

    return maxdiceroll

print(f"f(\"5233165554211\") returns {f('5233165554211')}")
print(f"f(\"2133\") returns {f('2133')}")