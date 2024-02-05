##### TIC TAC TOC GAME ######
### Developed by rogertxe ###
###### February 2024 ########

import os
import random

game_title = """                                                                                           
_/_/_/_/_/  _/                _/_/_/_/_/                        _/_/_/_/_/                   
   _/            _/_/_/          _/      _/_/_/    _/_/_/          _/      _/_/      _/_/    
  _/      _/  _/                _/    _/    _/  _/                _/    _/    _/  _/_/_/_/   
 _/      _/  _/                _/    _/    _/  _/                _/    _/    _/  _/          
_/      _/    _/_/_/          _/      _/_/_/    _/_/_/          _/      _/_/      _/_/_/                               

Play against the machine!

"""


def print_board(board):
    for row in board:
        print(' | '.join(row) + ' |')
        print('-' * 15)

def main():
    os.system('cls')
    print(game_title)
    board = [
        [' ', '1', '2', '3'],
        ['1', ' ', ' ', ' '],
        ['2', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ']
    ]
    print_board(board)
    
    player_symbol = choose_symbol()
    
    while True:
        player_move = choose_movement()
        if make_move(board, player_symbol, player_move):
            if check_winner(board, player_symbol):
                print("Congratulations! You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            computer_symbol = 'O' if player_symbol == 'X' else 'X'
            computer_move(board, computer_symbol)

            if check_winner(board, player_symbol):
                print("Congratulations! You win!")
                break
            elif check_winner(board, computer_symbol):
                print("Computer wins! Better luck next time.")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

def choose_symbol():
    while True:
        symbol = input("Choose 'O' or 'X' to play: ").upper()
        if symbol in ['O', 'X']:
            return symbol
        else:
            print("Invalid choice. Please choose 'O' or 'X'.")

def choose_movement():
    while True:
        movement = input("Choose row and column to move, e.g. 11, 23: ").upper()
        if movement in ['11', '12', '13', '21', '22', '23', '31', '32', '33']:
            return movement
        else:
            print("Invalid movement. Please choose a right combination of row and column.")

def make_move(board, symbol, position):
    row = int(position[0]) - 1
    col = int(position[1]) - 1
    
    if not check_empty(board, row, col):
        print("Invalid movement. The chosen position is not empty.")
        return False
    
    board[row + 1][col + 1] = symbol
    os.system('cls')
    print(game_title)
    print_board(board)
    return True

def check_empty(board, row, col):
    return board[row + 1][col + 1] == ' '

def computer_move(board, symbol):
    empty_positions = [(r, c) for r in range(1, 4) for c in range(1, 4) if check_empty(board, r - 1, c - 1)]
    
    if empty_positions:
        random_position = random.choice(empty_positions)
        make_move(board, symbol, f"{random_position[0]}{random_position[1]}")
        print(f"Computer moved to {random_position} position!")

def check_winner(board, symbol):
    # Check rows and columns
    for i in range(1, 4):
        if all(board[i][j] == symbol for j in range(1, 4)) or all(board[j][i] == symbol for j in range(1, 4)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(1, 4)) or all(board[i][4 - i] == symbol for i in range(1, 4)):
        return True

    return False


def is_board_full(board):
    for row in board[1:]:
        for col in range(1, 4):
            if row[col] == ' ':
                return False  # If any empty cell is found, the board is not full
    return True

os.system('cls')
while input("Would you like to play Tic Tac Toe (y/n) ") == "y":
    main()

