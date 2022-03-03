# M : 행 / N : 열
M, N = map(int, input().split())

chess = []
result = []


for i in range(M):
    chess.append(input())

# 정답을 미리 정해놓고(8*8에서 BWBWBW...)
# 정답과 다르면 CNT를 하기
# 이때, 시작점이 B인지, W인지에 따라 CNT를 나눠야함

for i in range(((M-8)+1)): # 행 반복
    for j in range((N-8)+1): # 열 반복
        startW_cnt = 0
        startB_cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess[k][l] != "B":
                        startB_cnt += 1
                    if chess[k][l] != "W":
                        startW_cnt += 1
                else:
                    if chess[k][l] != "B":
                        startW_cnt += 1
                    if  chess[k][l] != "W":
                        startB_cnt += 1
        result.append(min(startW_cnt,startB_cnt))
                        
print(min(result))
                        
    