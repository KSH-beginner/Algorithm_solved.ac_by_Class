N = int(input())

num = []

for i in range(N):
    num.append(int(input()))

num.sort()
#[-2, 1, 2, 3, 8]
    
avg = round(sum(num) / N)

mid = num[N//2]

num_range = max(num) - min(num)

new_num = [0 for _ in range(-4001, 4001)]

for i in range(N):
    X = num[i]
    new_num[X] += 1
    
max_num = max(new_num)

mode = []

for i in range(-4001, 4001):
    if new_num[i] == max_num:
        mode.append(i)
        
mode.sort()

print(mode)

if len(mode) == 1:
    mode_num = mode[0]
else:
    mode_num = mode[1]
    
    
    
print(avg)
print(mid)
print(mode_num)
print(num_range)
    
