'''
average case time complexity : O(n*n)
worst-case time complexity : O(n*n) 
best case time complexity : O(n)


'''


def insertionSort(nums):
    for i in range(1,len(nums)):
        valueToSort = nums[i]
        while nums[i-1]>valueToSort and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i = i-1
    return nums