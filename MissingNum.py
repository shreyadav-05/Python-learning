#Find Missing Number (1 to n)def missing_number(nums)
def missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

# Example
print(missing_number([1, 2, 4, 5, 6, 7,8]))




