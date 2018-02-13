import numpy as np 

# Coin Change
# https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
# Given a value N, if we want to make change for N cents, 
# and we have infinite supply of each of S = { S1, S2, .. , Sm}
#  valued coins, how many ways can we make the change? The order of coins doesn't matter.


X = [1,2,3]
N = 4

# X = [2, 5, 3, 6]
# N = 10

R = [[0 for j in range(len(X)+1)] for i in range(N+1)]


for i in range(1,N+1):
	R[i][0] = 0

for i in range(0,len(X)+1):
	R[0][i] = 1

for i in range(1,N+1):
	for j in range(1,len(X)+1):
		if X[j-1] > i:
			R[i][j] = R[i][j-1]
		else:
			R[i][j] = R[i][j-1] + R[i-X[j-1]][j]

print(np.matrix(R))
print R[-1][-1]