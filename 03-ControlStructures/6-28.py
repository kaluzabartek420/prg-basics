fibo_i_minus_2 = 0
fibo_i_minus_1 = 1
sequence = "0 1 "

for i in range(3, 21):
    fibo_i = fibo_i_minus_2 + fibo_i_minus_1
    sequence += str(fibo_i) + " "
    fibo_i_minus_2 = fibo_i_minus_1
    fibo_i_minus_1 = fibo_i

print(sequence)