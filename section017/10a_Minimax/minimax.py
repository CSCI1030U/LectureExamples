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

ttt = TicTacToe()
ttt.print()