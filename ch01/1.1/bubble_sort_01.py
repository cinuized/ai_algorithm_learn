'''
Bubble Sort basic
'''
import time

def bubble_sort(nums):
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1 ):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [7, 6, 3, 9, 1, 8]
print("Before Sorting: ", nums)
start = time.perf_counter()
bubble_sort(nums)
end = time.perf_counter()
print("After Sorting: ", nums)
print("Time-consuming: ", end - start)