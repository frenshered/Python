import random
import time
import math

N = 1000
D = 100

arr = []


def filling(A, n, d):
    print('Filling...')
    for i in range(n):
        k = random.randint(-d, d)
        A.append(k)
    print('The end')


start = math.floor(time.time())


# -- sorting №1 --
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp

    return i + 1


# -- sorting №2 --
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


filling(arr, N, D)

# quickSort(arr, 0, len(arr) - 1)
# insertionSort(arr)

print(arr)

end = math.floor(time.time())
print('Time: ', end - start, 's', sep='')
