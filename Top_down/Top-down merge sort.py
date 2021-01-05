# TOP DOWN IMPLEMENTATION
import time
def mergesort(ary):

    if len(ary)>1:
        mid = len(ary) // 2
        lft = ary[:mid]
        rgt = ary[mid:]
        mergesort(lft)
        mergesort(rgt)
        i=j=k=0
        while i < len(lft) and j < len(rgt):
            if lft[i] < rgt[j]:
                ary[k]=lft[i]
                i=i+1
            else:
                ary[k]=rgt[j]
                j=j+1
            k=k+1

        while i < len(lft):
            ary[k]=lft[i]
            i=i+1
            k=k+1

        while j < len(rgt):
            ary[k]=rgt[j]
            j=j+1
            k=k+1


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