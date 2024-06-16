from collections import deque



if __name__ == "__main__":
    n, w, L = map(int, input().split())

    truck = deque(list(map(int, input().split())))

    ## 은근 어렵다...

    bridge = deque([0 for _ in range(w)])
    times = 0

    while bridge:
        times += 1
        bridge.popleft() ## 하나 빼줌

        if truck: ## 대기중인 트럭이 있다면?
            if sum(bridge) + truck[0] <= L:
                bridge.append(truck.popleft())
                ## 현재 다리에 있는 트럭의 합이랑 들어올 트럭의 합이 더했을때 최대하중보다 작다면
                ## 트럭은 다리로 이동 가능
            else:
                bridge.append(0)

    print(times)

# https://tral-lalala.tistory.com/100