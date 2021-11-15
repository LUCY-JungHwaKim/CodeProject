T = int(input())

T = int(input())

N_ary = []

for i in range(T):
    N = int(input())
    N_ary.append(N)

N_ary = sorted(N_ary)

for i in range(len(N_ary)):
    print(N_ary[i])
