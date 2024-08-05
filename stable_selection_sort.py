# Stable selection sort

def stableSelectionSort(a, n):
    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        key = a[min_idx]

        while min_idx > i:
            a[min_idx] = a[min_idx-1]
            min_idx -= 1
        a[i] = key
    return a

a = [4,5,3,2,4,1]
n = len(a)

res = stableSelectionSort(a, n)
print("Sorted array is: ",a)
