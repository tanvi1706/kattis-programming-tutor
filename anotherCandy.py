n = int(input())

for test in range(0, n):
    input()
    candies = 0
    children = (int(input()))

    for t in range(0, children):
        candy = int(input())
        candies += candy

    remainder = candies % children

    if remainder == 0:
        print('YES')
    else:
        print('NO')