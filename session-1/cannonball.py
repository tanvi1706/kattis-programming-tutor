
import math
def amazing_cannonball(v0, theeta, x1, h1, h2):
    t = x1 / (v0 * math.cos(math.radians(theeta)))
    vertical_distance = (v0 * t * math.sin(math.radians(theeta))) - ((9.81 * t * t)/2)
    if vertical_distance > h1+1 and vertical_distance < h2-1:
        return "Safe"
    else:
        return "Not Safe"
    # return vertical_distance

n = int(input())
for i in range(n):
    v0, theeta, x1, h1, h2 = input().split(" ")
    print(amazing_cannonball(float(v0), float(theeta), float(x1), float(h1), float(h2)))
# v0, theeta, x1, h1, h2 = input().split(" ")
# print(amazing_cannonball(float(v0), float(theeta), float(x1), float(h1), float(h2)))