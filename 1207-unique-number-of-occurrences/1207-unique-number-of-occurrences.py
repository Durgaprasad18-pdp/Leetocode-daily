class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        h={}
        for i in arr:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        ans = set()        
        for i in h.keys():
            if h[i] in ans:
                return False
            else:
                ans.add(h[i])
        return True                
                               
        