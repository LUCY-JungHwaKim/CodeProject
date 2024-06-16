import heapq
import sys



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    hq = []

    for i in range(n):
        num = int(sys.stdin.readline())

        if num != 0:
            heapq.heappush(hq, (abs(num), num)) ## 절대값이 가장 작은 경우 출력, 요 부분 조심
        else:
            if hq: ## 빈배열이라면
                print(heapq.heappop(hq)[1])
            else:
                print(0)
