
import sys
T = int(sys.stdin.readline())

N_ary = []

for i in range(T):
    N = int(input())
    N_ary.append(N)

def heap_sort(N_ary):
    for i in range(len(N_ary)//2 - 1, -1, -1):
        heapify(N_ary, i, len(N_ary))

    for i in range(len(N_ary)-1, 0, -1):
        N_ary[0], N_ary[i] = N_ary[i], N_ary[0]
        heapify(N_ary, 0, i)

    return N_ary

def heapify(N_ary, index, heap_size):
    largest = index
    left_idx = 2*index + 1
    right_idx = 2*index + 2

    if left_idx < heap_size and N_ary[left_idx] > N_ary[largest]:
        largest = left_idx
    if right_idx < heap_size and N_ary[right_idx] > N_ary[largest]:
        largest = right_idx
    
    if largest != index:
        N_ary[largest], N_ary[index] = N_ary[index], N_ary[largest]
        heapify(N_ary, largest, heap_size)

N_ary = heap_sort(N_ary)
for i in range(len(N_ary)):
    print(N_ary[i])