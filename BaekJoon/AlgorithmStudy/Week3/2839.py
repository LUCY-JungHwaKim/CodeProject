N = int(input())

#봉지는 3kg, 5kg 두 종류
#간단한 문제였음..
#3을 한번씩 빼는걸 기준으로 가방개수 카운팅하고
#뺀 숫자가 5의 배수이면은 5로 나눈 몫을 가방 개수 카운팅에 다시 더해줌
#아주 간결한 문제였음..
#어렵게 생각하지 말기

bag_cnt = 0
while N >= 0:
    if N%5 == 0:
        bag_cnt += int(N/5)
        print(bag_cnt)
        break
    N -= 3
    bag_cnt += 1
else:
    print(-1)
