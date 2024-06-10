
if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N ,M = map(int, input().split())

        ary = []
        row_sums = [0] * N
        col_sums = [0] * N
        ## 미리 행, 열 합 구하기
        for i in range(N):
            tmp = list(map(int, input().split()))
            ary.append(tmp)

            row_sums[i] += sum(tmp) ## 행 합

            for j in range(N):
                col_sums[j] += tmp[j] ## 열합 구하기



        for _ in range(M):
            r1, c1, r2, c2, v = map(int, input().split())

            for x in range(r1-1, r2): ## 행 수 만큼 반복
                row_sums[x] += (c2-c1+1) * v  ## 열 차이 만큼 v값 더하면됨
            for x in range(c1-1, c2): # 열 수 만큼 반복
                col_sums[x] += (r2-r1+1) * v ## 행 차이만큼 v값 더하면됨
                


        print(" ".join(map(str ,row_sums)))
        print(" ".join(map(str, col_sums)))