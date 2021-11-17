import sys

T = int(sys.stdin.readline())

word_ary = []

for i in range(T):
    word_ary.append(sys.stdin.readline().strip())

word_ary = list(set(word_ary))
word_ary.sort() #알파벳 별 정렬
word_ary.sort(key=len)  #길이별 정렬

# 정렬 순서를 주의해야 되는데, 상위 조건 A와 하위 조건 B가 있으면
# 먼저 B로 정렬을 한 후에 A로 정렬을 해야 원하는 결과를 얻을 수 있다.

for i in word_ary:
    print(i)