N = int(input())
s_card = set(map(int, input().split()))

M = int(input())
card = list(map(int, input().split()))
lst = [0 for i in range(M)]

for i in range(M) :
    if card[i] in s_card :
        lst[i] += 1

for i in range(len(lst)) :
    print(lst[i])