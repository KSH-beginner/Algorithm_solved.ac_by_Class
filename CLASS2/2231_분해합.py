n = int(input())

for i in range(1, n+1):
    num = 0
    for j in range(len(str(i))):
        num += int(str(i)[j])

    new_num = i + num
    
    if new_num == n:
        print(i)
        break
    
    elif i == n:
        print(0)
        
     
                