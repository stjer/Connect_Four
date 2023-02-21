import os
ROW_COUNT = 7
COLUMN_COUNT = 7
deco = ['○','①','②']
def create_board():
    board = [[0 for _ in range(ROW_COUNT)] for _ in range(COLUMN_COUNT)]
    return board
board = create_board()
player = ["Player1","Player2"]

def print_board(board):
    os.system('cls')
    for row in reversed(range(ROW_COUNT)):
        row_string = ''
        for col in range(COLUMN_COUNT):
            try:row_string += f"{deco[board[col][row]]}"
            except:row_string += f"{board[col][row]}"
        print(row_string)
    print('')
    
#
def highlight(board, r,c):
    if board[r][c] == 1:
        board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = "❶"
    else:
        board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = "❷"

def is_valid_location(board, col):
    return board[col][ROW_COUNT-1] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[col][row] == 0:
            return row

def add_piece(board, col, piece):
    row = get_next_open_row(board, col)
    board[col][row] = piece

def check_win(board):
    
    # check horizontal win
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] and board[r][c] != 0:
                highlight(board,r,c)
                return True
    
    # check vertical win
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] and board[r][c] != 0:
                highlight(board,r,c)
                return True
    
    # check diagonal win (positive slope)
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] and board[r][c] != 0:
                highlight(board,r,c)
                return True
    
    # check diagonal win (negative slope)
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] and board[r][c] != 0:
                highlight(board,r,c)
                return True

    return False

def play_game():
    turn = 0
    game_over = False

    while not game_over:
        if turn == 0:
            col = int(input("Player 1's turn (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                add_piece(board, col, 1)
                turn = 1
        else:
            col = int(input("Player 2's turn (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                add_piece(board, col, 2)
                turn = 0

        print_board(board)
        if check_win(board)==True:
            if turn == 0:
                turn = 1
            else :
                turn = 0
            print_board(board)
            print(f"4목 완성, {player[turn]} 승리")
            break
    
    

            
play_game()
input()
