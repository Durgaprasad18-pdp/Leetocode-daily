class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = min(nums)
        b = max(nums)
        final = []
        for i in range(a,b+1,1):
            if i not in nums:
                final.append(i)
        return final        

            
    

        