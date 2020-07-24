'''

'getpivot' function is defined here to find the best pivot element in order to reduce the worst case complexity which is O(n*n)
Average performance :	O(n log n)
Best-case performance :	O(n log n) (simple partition) or O(n) (three-way partition and equal keys)
Worst-case performance : O(n2)
here A is the input array which we pass to the functions as argument

'''
def getPivot(A):
    low = 0
    high = len(A)
    mid = (low+high)//2
    pivot = high-1
    if A[low]<A[mid]:
        if A[mid]<A[high-1]:
            pivot = mid
    elif A[low]<A[high-1]:
        pivot = low
    return pivot
    

def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop(getPivot(A))
    items_smaller = []
    items_greater = []
    for i in A:
        if i > pivot:
            items_greater.append(i)
        else:
            items_smaller.append(i)
    return quick_sort(items_smaller)+[pivot]+quick_sort(items_greater)
