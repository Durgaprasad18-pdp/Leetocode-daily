class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        n = list(n)
        n.sort()
        ans = int(n[-1])*int(n[-2])
        return ans
        
          

        