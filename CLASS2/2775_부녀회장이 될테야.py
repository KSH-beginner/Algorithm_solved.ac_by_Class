import sys
input = sys.stdin.readline

T = int(input())

dp = []

for i in range(15):
    dp.append([0 for _ in range(15)])
    

for i in range(15):
    dp[0][i] = i
    
for j in range(15):
    dp[j][1] = 1


for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

    
for i in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])


