class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [None] * len(A)
        index = [0, 1] 
        for x in A:
            ans[index[x%2]] = x
            index[x%2] += 2
        return ans 