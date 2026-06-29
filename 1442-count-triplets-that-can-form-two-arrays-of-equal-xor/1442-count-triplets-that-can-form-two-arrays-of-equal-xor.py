class Solution:
    def countTriplets(self, arr) -> int:
        count = 0
        n = len(arr)
        for start in range(n - 1):
            res = arr[start]
            for end in range(start + 1, n):
                res = res^ arr[end]
                if not res:
                    count =count + end - start
        return count