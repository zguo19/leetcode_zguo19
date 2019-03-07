class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            n = target - nums[i]
            num2 = nums[(i+1):]
            if n in num2:
                return [i, num2.index(n)+i+1]
        return None