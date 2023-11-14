def perm(arr, n):
    result = []

    if n > len(arr):
        #print(result)
        return result

    if n == 1:
        for i in arr:
            #print(result)
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            #print(ans)
            ans.remove(arr[i])
            #print(ans)
            print(ans, n-1)
            for p in perm(ans, n-1):

                result.append([arr[i]]+p)
                print(result)
            print('-----------')

    return result

arr = [1,2,3]
print(perm(arr,3))