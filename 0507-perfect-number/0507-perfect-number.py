class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]

        # final = 0
        # if num<=1:
        #     return False
        # for i in range(1,num):
        #     if num%i==0:
        #         final = final+i
        # return final==num

        