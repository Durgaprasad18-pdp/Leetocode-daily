class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        ans = []
        for i in nums1:
            if i not in h.keys():
                h[i]=1
        for i in nums2:
            if i in h.keys():
                h[i]=h[i]+1
        for i in h.keys():
            if h[i]>1:
                ans.append(i)
        return ans                        
        