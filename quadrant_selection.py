def select_quadrant_x_y(x,y):
	if x > 0 and y > 0:
		print("1")
	elif x > 0 and y < 0:
		print("4")
	elif x < 0 and y > 0:
		print("2")
	elif x < 0 and y < 0:
		print("3")
	else:
		print("invalid")

x = int(input())
y = int(input())
select_quadrant_x_y(x,y)