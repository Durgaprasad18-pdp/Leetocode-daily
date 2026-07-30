class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMagazine = {}

        for ch in magazine:
            countMagazine[ch] = countMagazine.get(ch, 0) + 1

        for ch in ransomNote:
            if countMagazine.get(ch, 0) == 0:
                return False

            countMagazine[ch] -= 1

        return True