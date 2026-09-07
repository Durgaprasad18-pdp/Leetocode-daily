class Solution:
    def isPalindrome(self, n: int) -> bool:
        copy =n 
        rev = 0
        while(n>0):
            last = n%10
            n = n//10
            rev = (rev*10)+last
        if rev==copy:
            return True
        return False        
        