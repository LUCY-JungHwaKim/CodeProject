
strinp = list(input())

stacks = []
rslt = ''
chk = False ## 괄호 안의 여부 체크용

idx = 0

while idx < len(strinp):
    if strinp[idx] == "<" :
        idx += 1
        while strinp[idx] != ">": # 닫힌 괄호 만날 때까지
            idx += 1
        idx += 1

    elif strinp[idx].isalnum(): # 숫자나 알파벳을 만난다면
        strt = idx

        while idx < len(strinp) and strinp[idx].isalnum():
            ## 인덱스가 원래 문자열 길이보다 작고,
            ## 숫자나 알파벳이라면
            idx += 1
        tmpstr = strinp[strt:idx]
        tmpstr.reverse()
        strinp[strt:idx] = tmpstr

    else:## 그냥 공백인 경우
        idx += 1

print("".join(strinp))
## 내가 너무 복잡하게 생각한것같다