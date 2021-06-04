n,x = map(int, input().split())
goods = sorted(map(int, input().split()))
if n == 1:
    print('1')
elif goods[-1] + goods[-2] <= x:
    print(n)
else:
    for i,cost in enumerate(goods):
        if cost + goods[i + 1] > x:
            print(i + 1)
            break