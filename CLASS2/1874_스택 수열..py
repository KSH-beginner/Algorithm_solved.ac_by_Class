n = int(input())

count = 0
stack = []
result = []
is_able = True

for i in range(n):
    X = int(input())
    
    while count < X:
        stack.append(count+1)
        result.append("+")
        count += 1
        
    if stack[-1] == X:
        stack.pop()
        result.append("-")
    else:
        is_able = False
        continue
    

if is_able == False:
    print("NO")
else:
    # print("\n".join(result))
    print(*result, sep="\n")