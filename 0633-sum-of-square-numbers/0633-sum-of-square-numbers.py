class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [i * i for i in range(int(c ** 0.5) + 1)]

        for x in squares:
            target = c - x

            left, right = 0, len(squares) - 1

            while left <= right:
                mid = (left + right) // 2

                if squares[mid] == target:
                    return True
                elif squares[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False