class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        #Check row
        for row in board:
            row_map = {}
            for col in row:
                if col != '.':
                    if col in row_map:
                        return False
                    else:
                        row_map[col] = 1
        
        #Check col
        col = 0
        while col < col_len:
            row = 0
            col_map = {}
            while row < row_len:
                temp = board[row][col]
                if temp != '.':
                    if temp in col_map:
                        return False
                    else:
                        col_map[temp] = 1
                row += 1
            col += 1

        #Check box
        start_box_row = 0
        while start_box_row < row_len:
            start_box_col = 0
            while start_box_col < col_len:
                box_map = {}
                row = start_box_row
                while row < start_box_row + 3:
                    col = start_box_col
                    while col < start_box_col + 3:
                        temp = board[row][col]
                        if temp != '.':
                            if temp in box_map:
                                return False
                            else:
                                box_map[temp] = 1
                        col += 1
                    row += 1
                start_box_col += 3
            start_box_row += 3
        return True

        