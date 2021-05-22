contest = []
list_of_visited = []
score = 0
count = 0
n = input()
while n != "-1":
    x, y, z = n.split(" ")
    x = int(x)
    if z == "right":
        score += x
        count += 1
        for i in list_of_visited:
            if i == y:
                score += 20
    elif z == "wrong":
        list_of_visited.append(y)
    n = input()
print(f"{count} {score}")