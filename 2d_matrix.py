class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
