class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2 or len(nums)==3 or len(nums)==4 or len(nums)==5 or len(nums)==6 or len(nums)==7: 
            return nums.index(max(nums))   
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0         
        
        