class Solution(object):
    def removeElement(self, nums, val):

        i = 0  # position for valid elements

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
