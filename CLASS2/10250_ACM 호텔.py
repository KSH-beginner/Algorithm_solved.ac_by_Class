T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room = []
    
    for i in range(1, W+1):
        for j in range(1, H+1):
            if W < 10:
                num = str(j) + "0" + str(i)
                room.append(num)  
            else:
                if i < 10:
                    num = str(j) + "0" + str(i)
                    room.append(num) 
                else:
                    num = str(j) + str(i)
                    room.append(num) 
                    
                     
    print(room[N-1])
