class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        pick = 0
        ans = ""
        while(i<=len(word1)-1) and (j<=len(word2)-1):
            if pick ==0:
                ans = ans + word1[i]
                i = i+1
                pick = 1
            else:
                ans = ans + word2[j]
                j = j+1
                pick = 0

        while(i<=len(word1)-1):
            ans = ans +word1[i]
            i = i+1
        while(j<=len(word2)-1):
            ans = ans + word2[j]
            j= j+1
        return ans        