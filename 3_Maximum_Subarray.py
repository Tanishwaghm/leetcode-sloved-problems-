def max_subarray(nums):
    current = max_sum = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)

    return max_sum
