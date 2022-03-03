# A, B = input().split()

# A_reverse = []
# B_reverse = []

# for i in range(len(A)):
#     A_reverse.insert(0, A[i])

# for i in range(len(B)):
#     B_reverse.insert(0, B[i])

# A_reverse_num = int(A_reverse[0])*100 + int(A_reverse[1])*10 + int(A_reverse[2])
# B_reverse_num = int(B_reverse[0])*100 + int(B_reverse[1])*10 + int(B_reverse[2])

# if A_reverse_num > B_reverse_num:
#     print(A_reverse_num)
# else:
#     print(B_reverse_num)

A, B = input().split()

A_reverse = A[::-1]
B_reverse = B[::-1]

if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)