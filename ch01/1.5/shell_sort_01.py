'''
Shell sort
'''

import time

def shell_sort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):
            temp = nums[i]
            j = i - step
            while j >= 0 and nums[j] > temp:
                nums[j+step] = nums[j]
                j -= step

            nums[j+step] = temp
        step //= 2

list = [7, 4, 8, 5, 2, 0, 1, 9, 3, 6]
print(list)
start = time.perf_counter()
shell_sort(list)
end = time.perf_counter()
print(list)
print("Time-consuming: ", end - start)