class Solution:
    def licenseKeyFormatting(self, s, k) :
        # bước 1: xóa '-' và viết hoa
        s = s.replace("-", "").upper()
        
        res = ""
        count = 0
        
        # duyệt từ cuối về đầu
        for i in range(len(s) - 1, -1, -1):
            res = s[i] + res
            count += 1
            
            if count == k and i != 0:
                res = "-" + res
                count = 0
        
        return res