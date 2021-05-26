a,b,c = input().split(" ")
numbers = [int(a), int(b), int(c)]
numbers.sort()
dictionary = {"A": 0, "B": 0, "C": 0}
st = "ABC"
for i in range(len(st)):
    dictionary[st[i]] = numbers[i]
string_input = input()
result = []
for ch in string_input:
    result.append(dictionary[ch])
print(' '.join(str(x) for x in result))


# v0zxq4@gmail.com
