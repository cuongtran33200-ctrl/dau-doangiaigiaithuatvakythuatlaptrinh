class Solution:
    def intersection(self, nums1, nums2) :
        res = []
        
        for x in nums1:
            if x in nums2 and x not in res:
                res.append(x)
        
        return res