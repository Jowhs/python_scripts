#! usr/bin/python

def fibonacci(n):
	a,b = 0,1
	r = []
	while b < n:
		r.append(b)
		a,b = b, a+b
	return r
print fibonacci(123)
