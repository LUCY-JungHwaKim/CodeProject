# # ##### 이게 내가 작성한 코드
n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for m in range(60):
            if '3' in str(m)+str(j)+str(i): 
                ## 문자열을 다 합친 후에 3을 포함하는지 확인
                cnt += 1

print(cnt)


