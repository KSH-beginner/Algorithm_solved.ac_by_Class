N = int(input())

cur_num = 1
cnt = 1

while cur_num < N:
     cur_num += 6*cnt
     cnt += 1
     
print(cnt)
