class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows  = [0] * 9
        cols  = [0] * 9
        boxes = [0] * 9
        for r in range(9):
            row = board[r]
            for c in range(9):
                v = row[c]
                if v == '.':
                    continue
                bit = 1 << (ord(v) - 48)          # 48 == ord('0')
                b = (r // 3) * 3 + c // 3          # which 3x3 box
                if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                    return False                  # duplicate found
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
        return True
