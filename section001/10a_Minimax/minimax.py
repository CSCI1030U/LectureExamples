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
        for row_index in range(0, len(self.board)):
            for col_index in range(0, len(self.board[row_index])):
                print(f'| {self.board[row_index][col_index]} ', end='')
            print('|')
            print('+---+---+---+')

    def _find_common(self, a, b, c):
        # return a piece (X or O), if that piece 
        # occupies all three variables
        if a != ' ' and a == b and a == c:
            return a 
        else:
            return None

    def find_winner(self):
        # find any horizontal wins
        for row in self.board:
            common = self._find_common(row[0], row[1], row[2])
            if common:
                return common

        # find any vertical wins
        for col_index in range(len(self.board[0])):
            common = self._find_common(self.board[0][col_index], self.board[1][col_index], self.board[2][col_index])
            if common:
                return common

        # find any diagonal wins
        common = self._find_common(self.board[0][0], self.board[1][1], self.board[2][2])
        if common:
            return common 
        common = self._find_common(self.board[2][0], self.board[1][1], self.board[0][2])
        if common:
            return common
        
        # find a tie game
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return ' '
        
        return None  # tie game
    
    def opponent(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def pick_move(self, player):
        return self._pick_move(self.board, player)

    def _pick_move(self, board, player):
        best_score = -1000
        move_to_row = None 
        move_to_col = None 
        opponent = self.opponent(player)

        # check to see if the game is over
        winner = self.find_winner()
        if not winner:
            return None, None, 0
        elif winner == player:
            return None, None, 1
        elif winner == opponent:
            return None, None, -1
        
        # the game is not over
        # find the next move
        for row_index in range(len(board)):
            for col_index in range(len(board[row_index])):
                if board[row_index][col_index] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[row_index][col_index] = player
                    _, _, move_score = self._pick_move(new_board, opponent)
                    move_score *= -1
                    if move_score > best_score:
                        best_score = move_score
                        move_to_row = row_index
                        move_to_col = col_index
        return move_to_row, move_to_col, best_score

ttt = TicTacToe()
current_player = 'X'
while ttt.find_winner() == ' ':
    ttt.print()
    row, col, score = ttt.pick_move(current_player)
    if row and col:
        ttt.board[row][col] = current_player
    current_player = ttt.opponent(current_player)
ttt.print()