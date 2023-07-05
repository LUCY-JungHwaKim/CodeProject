n = 2260

cnt = 0

coins = [500, 100, 50, 10]

for con in coins:
    tmp_cal = n // con
    cnt += tmp_cal
    n %= con ## 남은 나머지를 다시 그 다음 동전으로 거스름돈 나누기

print(cnt)