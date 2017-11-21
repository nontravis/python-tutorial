'''
Project: Tic Tac Toe
Created Date: Friday November 03 2017
Author: TheKhaeng
-----
Last Modified:
Modified By:
-----
Copyright (c) 2017 TheKhaeng.io
'''
from __future__ import print_function  # For using the same code in either Python 2 or 3
import string
from IPython.display import clear_output

# Global variable
board = [" "] * 10
game_state = True
announce = ""


def reset_board():
    global board, game_state
    board = [" "] * 10      # NOTE: Game will ignore the 0 index
    game_state = True


def clear_board():
    clear_output()
    print(chr(27) + "[2J")


def display_board():
    clear_board()
    print(chr(27) + "[2J")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, position):
    return board[position] in list(string.whitespace)


def full_board_check(board):
    return " " not in board[1:]


def ask_player(mark):       # Asks player where to place X or O mark, checks validity
    global board
    req = "Choose where to place your: " + mark + " "
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1, 10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")
            continue


def player_choice(mark):
    global board, game_state, announce
    announce = ''       # Set game blank game announcement
    mark = str(mark)    # Get Player Input
    ask_player(mark)    # Validate input

    if win_check(board, mark):  # Check for player win
        clear_board()
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False

    clear_board()
    display_board()

    if full_board_check(board):
        announce = "Tie!"
        game_state = False

    return game_state, announce


def replay():
    return raw_input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


def play_game():
    reset_board()
    global announce

    # Set marks
    X = 'X'
    O = 'O'
    while True:
        clear_output()
        display_board()

        game_state, announce = player_choice(X)
        print(announce)
        if game_state == False:
            break

        # Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

    # Ask player for a rematch
    rematch = raw_input('Would you like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing!")


play_game()
