# 148 Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.


def find_min_max(*nums):
    min_num, max_num = nums[0], nums[0]

    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num


mm = find_min_max(1, 2, 3, 5, 6)
print('min = {} \nmax = {}'.format(*mm))

