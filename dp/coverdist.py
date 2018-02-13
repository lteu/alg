import numpy as np 

# Failed ...

# Count number of ways to cover a distance 1.9
# https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/

# Given a distance dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

# Input:  n = 3
# Output: 4
# Below are the four ways
#  1 step + 1 step + 1 step
#  1 step + 2 step
#  2 step + 1 step
#  3 step

# Input:  n = 4
# Output: 7


#initialize 
n = 10
R = [0 for j in range(n+1)] 
R[0] = 1;
R[1] = 1;
R[2] = 2;

for x in xrange(3,n+1):
	R[x] = R[x-1] + R[x-3] + R[x-2]

print R[-1]
# wrong answer

# n = 6

# # perfect partition problem
# # arr = [1, 6, 11, 5]
# # half = int(round(sum(arr)/2))

# R = [[0 for j in range(3)] for i in range(n)]

# # # initialize
# for i in range(n):
# 	R[i][0] = 1;
# for i in range(3):
# 	R[0][i] = 1;

# # # calculate
# for i in range(1,n):
# 	for j in range(1,3):
# 		R[i][j] = R[i-1][j-1] + R[i-1][j]

# print(np.matrix(R))

# print R[-1][-1]


