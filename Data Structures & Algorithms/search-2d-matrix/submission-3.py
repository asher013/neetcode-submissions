class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, m-1
        row = 0
        for i, mat_row in enumerate(matrix):
            if mat_row[0] <= target <= mat_row[m-1]:
                row = i
                break
        while l <= r:
            mid = l + ((r-l)//2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
