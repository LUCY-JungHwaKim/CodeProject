T = int(input())


result_str = []
for i in range(T):
    R, S = map(str, input().split())

    S = list(S)
    result_sent = ''
    for j in range(len(S)):
        result_sent += S[j]*int(R)
    result_str.append(result_sent)

for i in range(len(result_str)):
    print(result_str[i])