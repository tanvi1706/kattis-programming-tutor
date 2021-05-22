def triks(sequence, listing):
	for c in sequence:
		if c == 'C':
			if listing[0] == 1 and listing[2] == 0:
				listing[0] = 0
				listing[2] = 1
			elif listing[0] == 0 and listing[2] == 1:
				listing[0] = 1
				listing[2] = 0
		if c == 'A':
			if listing[0] == 1 and listing[1] == 0:
				listing[0] = 0
				listing[1] = 1
			elif listing[0] == 0 and listing[1] == 1:
				listing[0] = 1
				listing[1] = 0
		if c == 'B':
			if listing[1] == 1 and listing[2] == 0:
				listing[1] = 0
				listing[2] = 1
			elif listing[1] == 0 and listing[2] == 1:
				listing[1] = 1
				listing[2] = 0
	for i in range(len(listing)):
		if listing[i] == 1:
			return i + 1
sequence = input()
start = [1, 0, 0]
print(triks(sequence,start))