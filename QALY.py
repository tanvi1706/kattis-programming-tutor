def quality_of_life(quality_values):
	summ = 0
	for x in quality_values:
		summ += x[0]*x[1]

	return summ
values = []
l = []
number = int(input())
for n in range(number):
	x,y = input().split(' ')
	l.append([float(x), float(y)])
print(format(quality_of_life(l), ".3f"))