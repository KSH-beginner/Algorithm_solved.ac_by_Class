N = int(input())

word = []

for i in range(N):
    word.append(input())

word_set = set(word)    

word_dict = {}

for i in word_set:
    word_dict[i] = len(i)

sorted_word_dict = sorted(word_dict.items(), key = lambda item : (item[1], item[0]))

for i in range(len(word_set)):
    print(sorted_word_dict[i][0])     
