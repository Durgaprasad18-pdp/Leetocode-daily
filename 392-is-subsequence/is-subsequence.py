class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        j = 0
        for i in t:
            if i ==s[j]:
                j = j +1
            if len(s)==j:
                return True
        return False                
        