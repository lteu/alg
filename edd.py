import numpy as np 

# Edit Distance 3.3
# https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

# Given two strings str1 and str2 and below operations that can performed on str1.
# Insert
# Remove
# Replace

# 1
# str1 = "geek"
# str2 = "gesek"

# 1
# str1 = "cat"
# str2 = "cut"

# 3
str1 = "sunday"
str2 = "saturday"

R = [[0 for j in range(len(str2))] for i in range(len(str1))]

# initialize
R[0][0] = 0 if str1[0] == str2[0] else 1
for i in range(1,len(str2)):
	score = 0 if str1[0] == str2[i] else 1
	score_in = R[0][i-1] + score
	score_out = R[0][i-1] + 1
	R[0][i] = min(score_in,score_out)

for i in range(1,len(str1)):
	score = 0 if str1[0] == str2[i] else 1
	score_in = R[i-1][0] + score
	score_out = R[i-1][0] + 1
	R[i][0] = min(score_in,score_out)

# calculate
for i in range(1,len(str1)):
	for j in range(1,len(str2)):
		score = 0 if str1[i] == str2[j] else 1
		score_in = R[i-1][j-1] + score
		R[i][j] = min(R[i][j-1]+1,R[i-1][j]+1,score_in)

print(np.matrix(R))
print R[-1][-1]
