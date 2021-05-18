#!/usr/local/bin/python3
import random
print('n/2::3n+1')
#n = input('enter n'+"\n")

n = [2, 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107, 113, 131, 137, 149, 167, 173, 179, 191, 197, 227, 233, 239, 251, 257, 263, 269, 281]

runN = 1

for N in n:
	runN = runN*N*random.randint(n[0]**2,n[len(n)-1]**3)
#	print('runN:',runN)
n=runN**68
print('n=',n)
#exit()
i=0

while int(n)!=1:
	i+=1
	if (int(n)%2)==0:
		n=int(n)//2
	else:
		n=int(n)*3+1
	print(str(n).strip('.0'))

print('Total Loops:',i)
