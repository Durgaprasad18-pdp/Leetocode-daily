class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        diff = 0
        for i in range(1,len(nums)):
            n = nums[i]-nums[i-1]
            if n>diff:
                diff=n
        return diff        
        