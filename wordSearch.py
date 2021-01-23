class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
                
        return False
    
    def backtrack(self, row, col, word):
        if len(word) == 0:
            return True
        
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != word[0]:
            return False
        
        ret = False
        
        self.board[row][col] = '#'
        
        for rowOff, colOff in [(0,1),(1,0),(0,-1),(-1,0)]:
            ret = self.backtrack(row + rowOff, col + colOff, word[1:])
            if ret: break
        
        self.board[row][col] = word[0]
        
        return ret