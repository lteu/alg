import numpy as np 

# Maximum size square sub-matrix with all 1s
# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

M = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]


R = [[0 for i in range(len(M[0]))] for j in range(len(M))]

# initialize
for i in range(len(M[0])):
	R[0][i] = 1 if M[0][i] == 1 else 0

for i in range(len(M)):
	R[i][0] = 1 if M[i][0] == 1 else 0

for i in range(1,len(M)):
	for j in range(1,len(M[0])):
		if M[i][j] == 1:
			R[i][j] = 1 + min(R[i-1][j],R[i][j-1],R[i-1][j-1])


print(np.matrix(R))
print 'max sub square matrix dimension:',max([max(R[i]) for i in range(len(R))])

