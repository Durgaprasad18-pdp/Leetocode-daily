class Solution:
    def isPalindrome(self, n: int) -> bool:
        c = n
        rev = 0
        #boundary case if number is less than 0, directly return False        
        if n<0:
            return False
        while(n!=0):
            r = n%10
            n = n//10
            rev = rev *10
            rev = rev +r
        if rev==c:
            return True
        return False


               
             
        