from collections import deque

N, Q = map(int, input().split())

map_ary = [list(map(int, input.split())) for _ in range(2**N)]
shark_level = list(map(int, input().split()))
direction = [(-1, 0), (1,0), (0, -1), (0, 1)] # 순서대로 상, 하, 좌, 우

