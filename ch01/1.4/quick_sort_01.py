'''
Quick Sort
nums: To be sorted
start-end: Sorting section
'''

import time

def quick_sort(nums, start, end):
    if start < end:
        standard = nums[start]
        low = start
        high = end
        while low < high:
            while low < high and nums[high] >= standard:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < standard:
                low += 1
            nums[high] = nums[low]

        nums[low] = standard
        quick_sort(nums, start, low)
        quick_sort(nums, low + 1, end)

list = [6, 7, 4, 6, 3, 1, 5, 2]
s = time.perf_counter()
quick_sort(list, 0, len(list)-1)
e = time.perf_counter()
print(list)
print("time-consuming: ", e - s)