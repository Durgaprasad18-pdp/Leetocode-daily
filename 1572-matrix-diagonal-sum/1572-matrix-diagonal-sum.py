class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                n = len(mat[i])
                if i==j:
                    sum = sum +mat[i][j]
                else:
                    if i+j==n-1:
                        sum = sum +mat[i][j]
        return sum            

       

        