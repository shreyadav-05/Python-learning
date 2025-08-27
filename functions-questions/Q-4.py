#Find Second Largest Number
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

print(second_largest([10, 20, 4, 45, 99, 99]))
