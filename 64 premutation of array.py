class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)

        # Step 1: find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: if pivot exists
        if i >= 0:

            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # swap pivot and just larger element
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse right part
        left, right = i + 1, n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
