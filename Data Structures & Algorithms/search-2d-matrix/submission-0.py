class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        for row in range(rows):
            l = 0
            r = len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif target < matrix[row][mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False
                
