'''
Bubble Sort optimize 2
'''
import time

def bubble_sort(nums):
    r = range(0, len(nums) - 1)
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1 ):
            print("Round %d and Time %d " % (i+1, j+1), end="\n")
            if nums[j] > nums[j+1]:
                print("%d is bigger then %d and CHANGE the position." % (nums[j], nums[j+1]), end="\n")
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                sorted_mark = False
                last_change = j
            else:
                print("%d is smaller then %d and DO NOT change the position." % (nums[j], nums[j+1]), end="\n")
            print(nums)
        print("Round %d sorting result: \t" % ( i+1 ), nums)
        if sorted_mark:
            return
        print("Last change position: ", last_change)
        r = range(0, last_change)

nums = [1, 3, 2, 4, 5, 6]
print("Before Sorting: ", nums)
start = time.perf_counter()
bubble_sort(nums)
end = time.perf_counter()
print("After Sorting: ", nums)
print("Time-consuming: ", end - start)