N = int(input())

def recursive(N):
    
    if N <= 1:
        return N

    return recursive(N-1) + recursive(N-2)


print(recursive(N))