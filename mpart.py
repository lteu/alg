import numpy as np 

# Partition a set into two subsets such that the difference of subset sums is minimum
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

# Given a set of integers, the task is to divide it into two sets 
# S1 and S2 such that the absolute difference between their sums is minimum.

# Example
# Input:  arr[] = {1, 6, 11, 5} 
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12 
# Subset2 = {11}, sum of Subset2 = 11    

# perfect partition problem
arr = [1, 6, 11, 5]
half = int(round(sum(arr)/2))

R = [[0 for j in range(len(arr)+1)] for i in range(half+1)]

# # initialize
for i in range(0,len(arr)+1):
	R[0][i] = True;
for i in range(1,half+1):
	R[i][0] = False;

# # calculate
for i in range(1,half+1):
	for j in range(1,len(arr)+1):
		if arr[j-1] > i:
			R[i][j] = R[i][j-1]
		else:
			R[i][j] = R[i][j-1] or R[i-arr[j-1]][j-1]

print(np.matrix(R))

# min problem
arr_inter = [sum(R[i]) for i in range(half+1)]
last_nonzero_index = 0
for idx, item in enumerate(arr_inter):
    if item != 0:
        last_nonzero_index = idx

sum_val = sum(arr)
dff = abs((sum_val - last_nonzero_index) - last_nonzero_index)

print dff

