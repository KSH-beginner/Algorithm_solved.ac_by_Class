import math

N = int(input())

cnt = 0

num = [0 for _ in range(1001)]

num[1] = 1


for i in range(2, int(math.sqrt(1000))+1):
    for j in range(i+i, 1001, i):
        num[j] = 1
        
is_num = list(map(int, input().split()))

for i in range(N):
    if num[is_num[i]] == 0:
        cnt += 1
    
print(cnt)