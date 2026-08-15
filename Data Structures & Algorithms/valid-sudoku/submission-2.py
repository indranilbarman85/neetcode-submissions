class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        import numpy as np
        arr = np.array(board)
        board_np = np.where(arr == '.',  '0', arr).astype(int) 
        board_np_transposed=np.transpose(board_np)
        for i in range(len(board_np)):
            filtered=board_np[i][board_np[i] != 0]
            filtered_T=board_np_transposed[i][board_np_transposed[i] != 0]
            if len(np.unique(filtered)) != len(filtered) or len(np.unique(filtered_T)) != len(filtered_T):
                return False
        
        interval=3

        for i in range(3):
            for j in range(3):
                subarray = board_np[i*interval:(i+1)*interval, j*interval:(j+1)*interval]
                filtered = subarray[subarray != 0]
                if len(np.unique(filtered)) != len(filtered):
                    return False
        return True
