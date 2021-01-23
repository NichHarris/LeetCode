# https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0
        present = 0
        
        for i in range(len(s)):
            if s[i] == "A":
                absent += 1
                if absent >= 2:
                    return False
            elif s[i] == "L":
                late += 1
                if i >= 2:
                    if s[i-1] == "L" and s[i-2] == "L":
                        return False
            else:
                present += 1
            

        
        return True