string = input()
n = int(input())
for i in range(n):
    x,t = input().split()
    t = int(t)
    count = 0
    j = 0
    s = string
    while j < len(s):
        if x in s:
            count += 1
            s = s[j + len(x) + 1:]
            j = j + len(x) + 1
        else:
            j += 1

        if count == t:
            print(j + 1)
            break
        if j == len(s) - 1:
            print("-1")

    # for j,ch in enumerate(string):
    #     if ch in x:
    #         count += 1
    #     if count == t:
    #         print(j + 1)
    #         break
    #     if j == len(string) - 1:
    #         print("-1")
        
