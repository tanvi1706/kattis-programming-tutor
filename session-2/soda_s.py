possess, empty, req = input().split()
empty = int(possess) + int(empty)
req = int(req)
total = 0
while empty >= req:
    bottles = empty % req  # the new bottles bought
    empty = empty // req # remaining bottles
    total += empty
    empty += bottles
print(total)