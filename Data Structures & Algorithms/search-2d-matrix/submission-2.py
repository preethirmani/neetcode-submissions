class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left, right = 0, len(row) - 1
            if target < row[left]:
                return False
            elif target > row[right]:
                continue
            elif target < row[right]:
                while left <= right:
                    mid = (left+right) // 2
                    if target < row[mid]:
                        right = mid - 1
                    elif target > row[mid]:
                        left = mid + 1
                    else :
                        return True
            else:
                if target == row[left] or target == row[right]:
                    return True

                
            
        return False