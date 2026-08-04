class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = []
        count = 0
        for n in nums:
            len = 0
            while(n!=0):
                r = n%10
                n = n//10
                len = len +1
            if len%2==0:
                count = count +1
        return count        
       

                 
            
        