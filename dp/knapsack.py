import numpy as np 

# 0-1 Knapsack Problem) 3.3
# https://www.geeksforgeeks.org/knapsack-problem/

# Given weights and values of n items, put these items in 
# a knapsack of capacity W to get the maximum total value 
# in the knapsack. In other words, given two integer arrays 
# val[0..n-1] and wt[0..n-1] which represent values and weights 
# associated with n items respectively. Also given an integer 
# W which represents knapsack capacity, find out the maximum value 
# subset of val[] such that sum of the weights of this subset is
#  smaller than or equal to W. You cannot break an item, either 
#  pick the complete item, or don't pick it (0-1 property)

# perfect partition problem
val = [60,100,120,23,414]
wet = [10,20,30,21,5]
W = 50

R = [[0 for j in range(len(wet)+1)] for i in range(W+1)]

# # initialize
for i in range(0,len(val)+1):
	R[0][i] = 0;
for i in range(1,W+1):
	R[i][0] = 0;

# # calculate
for i in range(1,W+1):
	for j in range(1,len(val)+1):
		if wet[j-1] > i:
			R[i][j] = R[i][j-1]
		else:
			R[i][j] = max(R[i][j-1],R[i- wet[j-1]][j-1] + val[j-1])

print(np.matrix(R))

print R[-1][-1]

