'''
Worst case time : O(n)
Best case time : O(n)
Average case time : O(n)
Space : O(n)

'''

from collections import Counter

def countingSort(nums):
    new=[]
    count = Counter(nums)
    for n,count in sorted(count.items()):
        for _ in range(count):
            new.append(n)
    return new
