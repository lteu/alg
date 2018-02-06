import numpy as np 

# longest-increasing-subsequence
# https://www.geeksforgeeks.org/longest-increasing-subsequence/

# For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80] # 6
# arr = [3, 10, 2, 1, 20] # 3
# arr = [3, 2] # 1
# arr = [50, 3, 10, 7, 40, 80] # 4


maxlen = len(arr)
R = [[0 for j in range(len(arr))] for i in range(maxlen)]

# init
R[0][0] = arr[0]
for i in range(1,maxlen):
	R[0][i] = R[0][i-1] if R[0][i-1] < arr[i] else arr[i]

for i in range(1,maxlen):
	for j in range(1,maxlen):
		if i > j:
			R[i][j] = 0
			continue

		if R[i-1][j] < arr[j] and (arr[j] < R[i][j-1] or R[i][j-1] == 0):
			R[i][j] = arr[j]
		else:
			R[i][j] = R[i][j-1]

print(np.matrix(R))
Q = [R[i][-1] for i in range(len(R)) if R[i][-1]!=0]

print len(set(Q))
# print R
