from collections import Counter

class Solution:
    def intersect(self, nums1, nums2) :
        count1 = Counter(nums1)
        res = []
        
        for x in nums2:
            if count1[x] > 0:
                res.append(x)
                count1[x] -= 1
        
        return res