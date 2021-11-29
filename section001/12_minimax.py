import copy

class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    
    def print(self):
        print('+---+---+---+')
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[row_index])):
                print(f'| {self.board[row_index][col_index]} ', end='')
            print('|')
            print('+---+---+---+')

    def _find_common(self, a, b, c):
        if a == b and a == c and a != ' ':
            return a 
        else:
            return None
        
    def _find_winner(self, board):
        # check for horizontal wins
        for row in board:
            common = self._find_common(row[0], row[1], row[2])
            if common:
                return common 
        
        # check for vertical wins
        for col_index in range(len(board[0])):
            common = self._find_common(board[0][col_index], board[1][col_index], board[2][col_index])
            if common:
                return common 

        # check for diagonal wins
        common = self._find_common(board[0][0], board[1][1], board[2][2])
        if common:
            return common 
        common = self._find_common(board[0][2], board[1][1], board[2][0])
        if common:
            return common 

        # check for a tie game
        for row in board:
            for cell in row:
                if cell == ' ':
                    # game is not over yet
                    return ' ' 

        # tie game
        return None 

    def opposite_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def _pick_move(self, board, player):
        pass
    
    def pick_move(self, player):
        return self._pick_move(self.board, player)


ttt = TicTacToe()
current_player = 'X'
while ttt._find_winner(ttt.board) == ' ':
    ttt.print()
    r, c, score = ttt.pick_move(current_player)
    ttt.board[r][c] = current_player
    current_player = ttt.opposite_player(current_player)
ttt.print()
