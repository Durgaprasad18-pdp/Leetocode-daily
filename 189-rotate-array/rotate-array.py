class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums.reverse()
        def reverse(nums,start,end):
            while(start<end):
                nums[start],nums[end]=nums[end],nums[start]
                start= start+1
                end = end -1
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)        

        