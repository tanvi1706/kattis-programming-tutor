n = int(input())
arr = []
array = []
for i in range(n):
    line = input()
    while line != "":
        arr.append(int(line))
    else:
        array.append(arr)
        arr = []
    


print(array)