import operator

T = int(input())

word_ary = {}

for i in range(T):
    word = str(input())

    if word not in word_ary:
        word_ary[word] = len(word)
    else:
        pass
print(word_ary)
word_ary = sorted(word_ary.items(), key=operator.itemgetter(1))
print(word_ary)

word_ary = dict(word_ary)
N_ary = []
for key, value in word_ary.items():
    print(key, value)