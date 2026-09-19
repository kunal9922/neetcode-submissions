class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl = 0
        rr = len(matrix) - 1
        while rl <= rr:
            rowMid = (rl + rr) // 2
            if matrix[rowMid][0] <= target <= matrix[rowMid][len(matrix[0])-1]:
                l = 0
                r = len(matrix[0]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[rowMid][mid] == target:
                        return True
                    elif target < matrix[rowMid][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            elif target < matrix[rowMid][0]:
                rr = rowMid - 1
            else:
                rl = rowMid + 1
        return False