import sys
N = int(sys.stdin.readline())
score_ary = []
dp = []
for i in range(N):
    score_ary.append(int(input()))

if N  == 1: #계단 개수가 1개일 때
    print(score_ary[0]) #계단에 해당하는 점수 하나만 출력
elif N == 2:    #계단 개수가 2개일 때
    print(max(score_ary[0]+score_ary[1], score_ary[1])) #이전계딴 한번 밟는거랑, 그냥 한번에 지금계단 밟는거 두개중에 최대값 출력
else:   #계단 개수가 3개 이상일때
    #먼저 0~2에 해당하는 계단 최대값점수 구해서 dp에 메모리제이션 해줌
    dp.append(score_ary[0])
    dp.append(max(score_ary[0]+score_ary[1], score_ary[1]))
    dp.append(max(score_ary[0]+score_ary[2], score_ary[1]+score_ary[2]))

    #나머지는 다음과 같이 해줌
    #i를 기준으로 i-2일때 저장된 dp값과 현재 계단값
    #i-3일때 저장된 dp값과 현재 계단값, 현재 계단 앞 값 wnd max 구하기 
    for i in range(3,N):
        dp.append(max(dp[i-2]+score_ary[i], dp[i-3]+score_ary[i-1]+score_ary[i]))

    print(dp[N-1])
        