
sequence = input()

length = len(sequence)
lower_count = 0
upper_count = 0
special_count = 0
space_count = 0 

for x in sequence:
    if x == "_":
        space_count += 1
    elif ord(x) >= 97 and ord(x) <= 122:
        lower_count += 1
    elif ord(x) >= 65 and ord(x) <= 90:
        upper_count += 1
    else:
        special_count += 1

print("{:.16f}".format(space_count/length))
print("{:.16f}".format(lower_count/length))
print("{:.16f}".format(upper_count/length))
print("{:.16f}".format(special_count/length))

