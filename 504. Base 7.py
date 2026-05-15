class Solution:
    def convertToBase7(self, num) :
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        res = ""

        while num > 0:
            res = str(num % 7) + res
            num //= 7

        return sign + res