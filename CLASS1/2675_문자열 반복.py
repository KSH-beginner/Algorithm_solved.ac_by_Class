T = int(input())

for i in range(T):
    R, S = input().split(" ")
    for i in range(len(S)):
        if i == len(S)-1:
            print(S[i] *int(R))
        else:
            print(S[i] *int(R), end="")


    


