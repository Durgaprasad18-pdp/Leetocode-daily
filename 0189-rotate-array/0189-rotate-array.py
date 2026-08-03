class Solution:
    def rotate(self, nums: List[int], r: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = r%len(nums)
        nums[:] =nums[len(nums)-r:]+nums[0:len(nums)-r-1+1]
        
        
        