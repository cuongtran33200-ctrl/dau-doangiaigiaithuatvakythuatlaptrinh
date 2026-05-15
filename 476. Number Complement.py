class Solution:
    def findComplement(self, num) :
        # đổi sang nhị phân (bỏ '0b')
        b = bin(num)[2:]
        
        # đảo bit
        res = ""
        for ch in b:
            if ch == '0':
                res += '1'
            else:
                res += '0'
        
        # đổi lại về số
        return int(res, 2)