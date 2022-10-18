import sys
N = int(input())


## 문제 내에서
## () 이 안에 () 요게 또 있고 또 있어야함
## 이중반복문 안쓰면 좋겠지만 무조건 안써야 된다고 생각하지말기


for i in range(N):
    str_ipt = sys.stdin.readline() # 문자열 입력
    check = 0
    vps_lst = []
    for j in range(len(str_ipt)-1): # 엔터까지 입력되므로 사이즈 1개 더 적게 시행
        #print(j,str_ipt[j])
        if str_ipt[j] == '(': ## 왼쪽 괄호면 삽입
            vps_lst.append('(')

        elif str_ipt[j] == ')': ## 오른쪽 괄호면
            if len(vps_lst) == 0: ## pop하기전에 스택에 아무것도 없으면
                check -= 1 # 체킹 한번 해줌
                break
            else: ## 왼쪽 괄호 한짝 pop --> 자기 짝 찾아가는거
                vps_lst.pop()
    if check == -1 or len(vps_lst) != 0:
        print("NO")
        # 스택에 아무것도 없거나 (( 이렇게 왼쪽 괄호들만 남았을 때
    else: # 아니면 VPS 맞음
        print("YES")

    # 밑에는 내가 잘못 이해한 코드
    # () 이거를 입력한대로 정렬하고 각 괄호의 개수가 같으면
    # YES인줄알았음
    # vps_sort = sorted(str_ipt[:-1])
    # #print(vps_sort)
    #
    # half_p1 = [i for i in vps_sort if i == '(']
    # half_p2 = [i for i in vps_sort if i == ')']
    #
    # if len(half_p1) == len(half_p2):
    #     print('YES')
    # else:
    #     print('NO')