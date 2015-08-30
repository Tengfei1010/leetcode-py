# this solution test time is 48ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        d = {}
        for i in range(0, length):
            current = nums[i]
            if current in d:
                return d[nums[i]] + 1, i + 1
            d[target - current] = i


