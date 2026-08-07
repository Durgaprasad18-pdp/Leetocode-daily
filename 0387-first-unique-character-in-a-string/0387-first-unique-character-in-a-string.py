class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in s:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        for i in range(0,len(s),1):
            if h.get(s[i])==1:
                return i
        return -1                    