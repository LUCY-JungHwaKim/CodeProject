N = int(input())

def recursive(N):
    result = 1
    if N == 0:
        return result
    else:
        result = N*recursive(N-1)

    return result

print(recursive(N))