class Solution:
    def checkRecord(self, s) :
        countA = 0
        countL = 0

        for ch in s:
            if ch == 'A':
                countA += 1
                if countA >= 2:
                    return False
            
            if ch == 'L':
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0  # reset nếu không phải L
        
        return True