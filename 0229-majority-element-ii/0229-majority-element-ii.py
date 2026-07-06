class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        for i in nums:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        ans = []
        for i in h.keys():
            if h[i]>(len(nums)/3):
                ans.append(i)
        return ans                    
        