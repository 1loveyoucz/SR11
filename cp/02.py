text_1 = input().split()
text_2 = input().split()
text_3 = input().split()

answ = [i for i in text_2 if (i not in text_1) and (i not in text_3)]
word_min = len(answ[0])

for word in answ:
    if len(word) < word_min:
        word_min = len(word)

print('-'.join(answ))
print(word_min)