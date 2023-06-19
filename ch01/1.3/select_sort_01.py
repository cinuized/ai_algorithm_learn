'''
Select Sort
'''

import time

def select_sort(nums):
    for i in range(0, len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            temp = nums[min_index]
            nums[min_index] = nums[i]
            nums[i] = temp


list = [3, 5, 1, 8, 6, 9, 7, 0, 2]
start = time.perf_counter()
select_sort(list)
end = time.perf_counter()
print(list)
print("Time-consuming: ", end - start)