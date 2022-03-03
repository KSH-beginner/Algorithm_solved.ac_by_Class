word = input()

upper_word = word.upper()

A = set(upper_word)
B = list(A)
dic = {}

for i in range(len(B)):
    dic[B[i]] = upper_word.count(B[i])
    
sort_dic = sorted(dic.items(), key = lambda x : -x[1])

if len(upper_word) == 1:
    print(upper_word)
else:
    if dic[sort_dic[0][0]] == dic[sort_dic[1][0]]:
        print("?")
    else:
        print(sort_dic[0][0])

