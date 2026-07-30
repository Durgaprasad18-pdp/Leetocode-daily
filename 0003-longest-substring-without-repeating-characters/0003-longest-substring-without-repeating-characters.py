class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        temp = ""

        for i in s:
            if i not in temp:
                temp = temp + i
            else:
                if len(temp) > len(ans):
                    ans = temp
                x = temp.index(i)
                temp = temp[x + 1:]
                temp = temp + i

        if len(temp) > len(ans):
            ans = temp

        return len(ans)