class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=nums.copy()
        suf=nums.copy()
        prod =1
        for i in range(len(nums)):
            prod = prod*nums[i]
            pre[i]=prod
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            prod = prod*nums[i]
            suf[i]=prod

        if len(nums)==2:
            nums[0]=suf[1]
            nums[1]=pre[0]

        nums[0]=suf[1]
        nums[len(nums)-1] = pre[len(nums)-2]

        for i in range(1,len(nums)-1):
            nums[i]=pre[i-1]*suf[i+1]           
        return nums