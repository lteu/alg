# Longest Common Subsequence
# https://www.geeksforgeeks.org/longest-common-subsequence/

# s1 = 'ABCDGH'
# s2 = 'AEDFHR'

s1 = 'AGGTAB'
s2 = 'GXTXAYB'
R = []

# setup
R = [[0 for i in range(len(s2))] for j in range(len(s1))]

for i in range(len(s1)):
    R[i][0] = 1 if s1[i] == s2[0] else 0

for i in range(len(s2)):
    R[0][i] = 1 if s1[0] == s2[i] else 0

for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        tmp = 1 if s1[i] == s2[j] else 0
        R[i][j] = max([R[i][j-1],R[i-1][j],R[i-1][j-1]]) + tmp

print R[-1][-1]
