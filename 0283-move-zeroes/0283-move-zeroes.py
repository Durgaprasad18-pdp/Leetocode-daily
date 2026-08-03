class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in nums:
            if i!=0:
                nums[j]=i
                j = j+1
        while(j<=len(nums)-1):
            nums[j]=0
            j = j+1        
        """
        Do not return anything, modify nums in-place instead.
        """
        