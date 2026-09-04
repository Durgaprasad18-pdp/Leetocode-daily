class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h={}
        for i in range(0,len(s)):
            if s[i] in h.keys() and h.get(s[i])!=t[i]:
                return False
            elif s[i] not in h.keys() and t[i] in h.values():
                return False
            else:
                h[s[i]]= t[i]

        return True                