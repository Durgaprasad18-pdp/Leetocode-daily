class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        for i in range(1,n+1,1):
            sum1 = sum1 +i
        sum2 = 0
        for i in nums:
            sum2 = sum2 +i
        return sum1-sum2        