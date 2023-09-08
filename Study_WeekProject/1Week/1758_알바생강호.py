n = int(input())

tips = []

for i in range(n):
    tips.append(int(input()))

tips.sort(reverse=True) ### 큰 숫자대로 정렬
## 받을 수 있는 최대값을 구하려면
## 팁을 더 받을 수 있게 주려는 팁을 많이 가진 사람을 제일 앞 순위로 선정해주면됨

final_tips = 0
for i in range(len(tips)):
    #print(tips[i], i)
    cur_tip = tips[i] - i
    if cur_tip <= 0: ## 음수 값 처리
        cur_tip = 0
    #print(cur_tip)
    final_tips += cur_tip

print(final_tips)