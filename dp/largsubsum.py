import numpy as np 

# Largest Sum Contiguous Subarray
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Write an efficient C program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.


X = [-2, -3, 4, -1, -2, 1, 5, -3]

R = [0 for i in range(len(X))]

R[0] = X[0]


for i in range(1,len(X)):
	R[i] = max(X[i], X[i] + R[i-1])

print R
print max(R)
