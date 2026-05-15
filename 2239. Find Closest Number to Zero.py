class Solution:
    def findClosestNumber(self, nums):
        res = nums[0]

        for x in nums:
            if abs(x) < abs(res):
                res = x
            elif abs(x) == abs(res) and x > res:
                res = x

        return res