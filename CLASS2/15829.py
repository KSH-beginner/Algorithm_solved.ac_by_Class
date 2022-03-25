L = int(input())

word = input()

sum_list = []

for i in range(len(word)):
    add_num = (ord(word[i]) - 96) * (31 ** i)
    sum_list.append(add_num)
    
print(sum(sum_list) % 1234567891)