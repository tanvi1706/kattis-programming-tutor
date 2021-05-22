def coldput(temperatures):
	count = 0
	for t in temperatures:
		if t < 0:
			count += 1
	return count



number = int(input())
x = [int(i) for i in list(input().split())]
print(coldput(x))

