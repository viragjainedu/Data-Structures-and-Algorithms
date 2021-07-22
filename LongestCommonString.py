"""
  A B C D G H
A 1 0 0 0 0 0 
C 0 0 1 0 0 0
D 0 0 0 1 0 0
G 0 0 0 0 1 0
H 0 0 0 0 0 1
R 0 0 0 0 0 0
X 0 0 0 0 0 0
"""

def LongestCommonSubstring(s1,s2):
    dp = [[0 for x in range(len(s1))]  for y in range(len(s2))]
    max = 0
    for i in range(len(s2)):
        for j in range(len(s1)):
            if(s2[i] == s1[j]):
                m=i-1
                n=j-1
                if(m<0):m=0
                if(n<0):n=0
                dp[i][j] = dp[m][n] + 1
                if(dp[i][j] >= max):
                    max = dp[i][j]

    print(dp)
    print(max)

if __name__ == '__main__':
    s1 = input("Enter String 1: ")
    s2 = input("Enter String 2: ")
    LongestCommonSubstring(s1,s2)