import numpy as np 

# Subset Sum Problem 3.4
# https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.  

# perfect partition problem
arr = [1, 2, 3, 4,2,6,7,3,2,50,100,3]
sum_val = 18

R = [[0 for j in range(len(arr)+1)] for i in range(sum_val+1)]

# # initialize
for i in range(0,len(arr)+1):
	R[0][i] = True;
for i in range(1,sum_val+1):
	R[i][0] = False;

# # calculate
for i in range(1,sum_val+1):
	for j in range(1,len(arr)+1):
		if arr[j-1] > i:
			R[i][j] = R[i][j-1]
		else:
			R[i][j] = R[i][j-1] or R[i- arr[j-1]][j-1]

print(np.matrix(R))

print R[-1][-1]

