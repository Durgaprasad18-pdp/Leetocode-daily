class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[len(nums)-1]
        ans = []
        for i in range(1,b+1,1):
            if a%i==0 and b%i==0:
                ans.append(i)
        return ans[len(ans)-1]        

        