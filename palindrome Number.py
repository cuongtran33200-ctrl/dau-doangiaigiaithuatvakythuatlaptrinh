class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev= rev * 10 + x % 10
            x //= 10
        return rev == x or rev // 10 == x

        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        # reverted = 0
        # while x > reverted:
        #     reverted = reverted * 10 + x % 10
        #     x //= 10
        # return x == reverted or x == reverted // 10