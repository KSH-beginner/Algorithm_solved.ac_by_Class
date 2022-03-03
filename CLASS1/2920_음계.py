scale = [1, 2, 3, 4, 5, 6, 7, 8]
sort_scale_reverse = sorted(scale, reverse=True)


N = list(map(int, input().split()))

if N == scale:
    print("ascending")
elif N == sort_scale_reverse:
    print("descending")
else:
    print("mixed")
    
    