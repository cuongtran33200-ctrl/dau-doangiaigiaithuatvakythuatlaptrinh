class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for x in nums1:
            found = False
            for i in range(len(nums2)):
                if nums2[i] == x:
                    found = True
                elif found and nums2[i] > x:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)

        return ans