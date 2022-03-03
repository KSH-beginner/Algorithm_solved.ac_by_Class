import math
M, N = map(int, input().split())

num = [0 for i in range(1000001)]
num[0] = 1
num[1] = 1

for i in range(2, int(math.sqrt(1000000))+1):
    for j in range(i+i, 1000001, i):
        num[j] = 1
        
for k in range(M, N+1):
    if num[k] == 0:
        print(k)
        
    