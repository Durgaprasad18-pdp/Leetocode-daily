class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                ans.append(i)
            elif len(ans)!=0 and ans[len(ans)-1]=='(' and i ==')':
                ans.pop()
            elif len(ans)!=0 and ans[len(ans)-1]=='[' and i==']':
                ans.pop()
            elif len(ans)!=0 and ans[len(ans)-1]=='{' and i=='}':
                ans.pop()
            else:
                return False
        if len(ans)==0:
            return True
        return False                            
        