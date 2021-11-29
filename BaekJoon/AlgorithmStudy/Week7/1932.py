N = int(input())


dp = [0 for i in range(2*(N-1))]

if N == 1:
    num = int(input())
    print(num)
else:

    for i in range(N):
        num_ary = list(map(int, input().split()))
        if i == 0:
            dp[0] = num_ary[0]
            continue
        else:
            new_ary = [0 for i in range(len(num_ary))]

            if len(new_ary) == 2:
                for j in range(len(new_ary)):
                    new_ary[j] = dp[0] + num_ary[(j+(j%2))//2]
                
            else:
                for j in range(len(new_ary)):
                    if j == 0:
                        new_ary[j] = dp[j] + num_ary[j]
                    elif j == len(new_ary)-1:   #처음이랑 끝은 거기에 해당하는 인덱스끼리 더해주고
                        new_ary[j] = dp[j-1] + num_ary[j]
                    else:   # 중간 사이에 있는것들은 최대값 구해서 최대값만 다시 메모리제이션 해줌
                        #굳이 전부의 경우 다해줄 필요 없음
                        if dp[j-1] + num_ary[j] < dp[j] + num_ary[j]:
                            new_ary[j] = dp[j] + num_ary[j]
                        else:
                            new_ary[j] = dp[j-1] + num_ary[j]
            
            for m in range(len(new_ary)):
                dp[m] = new_ary[m]
            #print(dp)
        
    print(max(dp))