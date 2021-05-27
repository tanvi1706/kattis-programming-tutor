h, w, n = input().split()
h = int(h)
w = int(w)
n = int(n)
height = 0
width = 0
completed = False
numbers = [int(i) for i in input().split()]
for x in numbers:
    if height < h:
        width += x
        if width == w:
            height += 1
            width = 0
        elif width > w:
            height = h + 1
        if height == h:
            completed = True
            
if completed:
    print("YES")
else:
    print("NO")

