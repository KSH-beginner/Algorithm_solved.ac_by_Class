import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())


print(V-A + (A-B))
