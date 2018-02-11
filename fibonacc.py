import numpy as np 

# fibonacci
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
#  Fn = Fn-1 + Fn-2


n = 9

R = [0 for i in range(n+1)]
R[0] = 0
R[1] = 1

for i in range(2,n+1):
	R[i] = R[i-1]+R[i-2]

print R[-1]
