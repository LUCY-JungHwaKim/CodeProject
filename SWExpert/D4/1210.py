for test_case in range(10):
    # ///////////////////////////////////////////////////////////////////////////////////
	n = int(input())
	data = list(list(map(int, input().split())) for i in range(100))
	goal_num = data[99].index(2)
	x,y = 99, goal_num
	visited = [[0] * 100 for _ in range(100)]
	answer = 0
	while x >= 0:
		visited[x][y] = 1	#y가 좌우 방향 이동
		if y-1>= 0 and data[x][y-1] ==1 and visited[x][y-1] == 0:	#골부터 거꾸로 가면서 좌우에 방문사항이 있는지 검토, 그리고 양옆의 값이 1인지 검토
			y -=1
		elif y+1<100 and data[x][y+1] ==1 and visited[x][y+1] == 0:	#얘도 마찬가지로
			y += 1
		else:	#둘다 값이 없으면 한칸 위로 땅기기
			x -= 1
	
	answer = y
	print("#"+str(test_case+1), answer)    