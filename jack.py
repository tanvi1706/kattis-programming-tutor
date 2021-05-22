def function_u(n,t,m):
	return n*t*m

n,t,m = input().split(' ')
print(function_u(int(n),int(t),int(m)))