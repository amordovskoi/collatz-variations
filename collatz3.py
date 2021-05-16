#!/usr/local/bin/python3
import decimal
decimal.getcontext().prec = 1000
import random

def down_to_one(n, x):

	print('n =', n)
	n_orig = n
	i=0
	while n!=1:
		print(n)
		i+=1
		if (n%2)==0:
			n=n//2
		else:
			n = (2**x)*n+2**x
	return i


n = 54717			## - starting number n
x = 13111			## - any integer

print('1 : Total Steps:', down_to_one(n, x))
print('n =', n, ', x =', x)
