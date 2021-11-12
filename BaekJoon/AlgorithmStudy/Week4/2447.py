N = int(input())


star = "***\n* *\n***\n"

print(star)

def recursive(N):
    N = int(N/3)

    for i in range(N):
        for j in range(N):
            print(star, end="")
        

recursive(9)