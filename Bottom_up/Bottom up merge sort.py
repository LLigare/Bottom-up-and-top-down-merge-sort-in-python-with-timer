# BOTTOM UP IMPLEMENTATION
import time
def merge(ary, temp, lft, mid, rgt):
    k = lft
    i = lft
    j = mid + 1

    # merge elements
    while i <= mid and j <= rgt:
        if ary[i] < ary[j]:
            temp[k] = ary[i]
            i = i + 1
        else:
            temp[k] = ary[j]
            j = j + 1
        k = k + 1

    while i < len(ary) and i <= mid:
        temp[k] = ary[i]
        k = k + 1
        i = i + 1

    for i in range(lft, rgt + 1):
        ary[i] = temp[i]


# Iteratively sort array using temporary list
def mergesort(ary):
    low = 0
    high = len(ary) - 1

    temp = ary.copy()

    # divide the list into blocks of size m
    # m = [1, 2, 4, 8, 16...]

    m = 1
    while m <= high - low:

        # for m = 1, i = [0, 2, 4, 6, 8...]
        # for m = 2, i = [0, 4, 8, 12...]
        # for m = 4, i = [0, 8, 16...]
        # ...

        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            merge(ary, temp, frm, mid, to)

        m = 2 * m


# Iterative Implementation of mergesort algorithm
if __name__ == '__main__':
    ary = [9, 4, 6, 3, 5, 1, 7, 2, 0, 8]

    print("Original Array :", ary)
    mergesort(ary)
    print("Modified Array :", ary)

# Adding a timer
time1 = time.perf_counter()
mergesort(ary)
time2 = time.perf_counter()
elapsed = time2 - time1

print('Time elapsed in seconds: ', round(elapsed, 10))