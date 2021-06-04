num = int(input())
sequence = input()
dictionary = { "Adrian": "ABC", "Bruno": "BABC", "Goran": "CCAABB" }
counts = {"Adrian": 0, "Bruno": 0, "Goran": 0}
for y in dictionary.keys():
    x = dictionary[y]
    len_x = len(x)
    for i in range(len(sequence)):
        if x[i % len_x] == sequence[i]:
            counts[y] += 1
# if len(list(set(list(counts.values())))) == 1:
#     print(counts["Adrian"])
#     for x in counts.keys():
#         print(x)
# else:
#     name = max(counts, key=counts.get)
#     print(counts[name])
#     print(name)
# print(counts.keys())
maximum = max(counts, key=counts.get)
print(counts[maximum])
for name in counts.keys():
    if counts[name] == counts[maximum]:
        print(name)





#         B A A C C
#Adrain:  A B C A B
#Bruno:   B A B C B
#         C C A A B