
N = list(map(int, input().split()))

square = pow(N[0], 2) + pow(N[1], 2) + pow(N[2], 2) + pow(N[3], 2) + pow(N[4], 2)

result = square % 10
print(result)