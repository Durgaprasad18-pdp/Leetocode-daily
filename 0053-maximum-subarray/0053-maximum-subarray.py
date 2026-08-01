class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        psum = []
        psum.append(nums[0])
        for i in range(1,len(nums)-1+1,1):
            x = max(psum[i-1]+nums[i],nums[i])
            psum.append(x)
        return max(psum)    
        