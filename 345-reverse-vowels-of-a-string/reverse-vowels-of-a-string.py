class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        i = 0
        j = len(a) - 1

        while(i < j):

            while(i <= len(a) - 1):
                if a[i] == 'A' or a[i] == 'E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U':
                    break
                elif a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
                    break
                i = i + 1

            while(j >= 0):
                if a[j] == 'A' or a[j] == 'E' or a[j] == 'I' or a[j] == 'O' or a[j] == 'U':
                    break
                elif a[j] == 'a' or a[j] == 'e' or a[j] == 'i' or a[j] == 'o' or a[j] == 'u':
                    break
                j = j - 1

            if(i < j):
                a[i], a[j] = a[j], a[i]
                i = i + 1
                j = j - 1

        return "".join(a)