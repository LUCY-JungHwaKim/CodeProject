from collections import deque

N, K = map(int, input().split())

belt_queue = deque(map(int, input().split()))



#belt_queue.rotate(1)    #오른쪽으로 한칸 회전 
robot_queue = deque([0]*N)


step = 0

while belt_queue.count(0) < K:

    belt_queue.rotate(1)
    robot_queue.rotate(1)

    robot_queue[-1] = 0 #마지막에 위치한 로봇은 항상 내림

    if robot_queue.count(1) != 0:   #로봇이 존재할 때
        for i in range(N-2, -1, -1):
            if robot_queue[i] and not robot_queue[i+1] and belt_queue[i+1]: #로봇이 존재하고, 다음 칸에 로봇이 없고, 벨트의 내구성이 있을 때
                belt_queue[i+1] -= 1
                robot_queue[i+1], robot_queue[i] = 1,0
        robot_queue[-1] = 0     #위에서 바꿔줫으니깐 또 항상내림

    if not robot_queue[0] and belt_queue[0]:    #첫번째 칸에 로봇이 없고, 벨트의 내구성이 있을때 로봇을 올려줌
        robot_queue[0] = 1
        belt_queue[0] -= 1

    step += 1

print(step)