'''
 Worst-case performance: O(N^2)
'''


def bubbleSort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1] = temp
    return nums
