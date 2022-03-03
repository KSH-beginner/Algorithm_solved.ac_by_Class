T = int(input())

for i in range(T):
    
    N, M = map(int, input().split())

    prior = list(map(int, input().split()))

    target_prior = [0 for i in range(N)]

    target_prior[M] = "target"

    cnt = 0
    while True:
        if max(prior) == prior[0]:
            prior.pop(0)
            cnt += 1
            
            if target_prior[0] == "target":
                print(cnt)  
                break
            
            else:
                target_prior.pop(0)
            
        else:
            prior.append(prior.pop(0))
            target_prior.append(target_prior.pop(0))
        


