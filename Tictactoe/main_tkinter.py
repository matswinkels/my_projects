""" Tic Tac Toe - vs AI; tkinter version """

import random
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def welcome_message():
    print('\n\nWELCOME TO THE TIC TAC TOE GAME!')
    print(1, 2, 3)
    print(4, 5, 6)
    print(7, 8, 9)
    print()

def end_message(score):
    if score == 0:
        print("IT'S A TIE!")
    elif score == 1:
        print('CONGRATULATIONS PLAYER. YOU WIN!')
    else:
        print('COMPUTER WINS!')

def print_board(board):
    print(*[board[x] for x in range(3)], sep='   ', end='\n\n')
    print(*[board[x] for x in range(3, 6)], sep='   ', end='\n\n')
    print(*[board[x] for x in range(6, 9)], sep='   ', end='\n\n')

def is_square_empty(board, move):
    return board[move - 1] != 'X' and board[move - 1] != 'O'

def is_board_full(board):
    return board.count('X') + board.count('O') == 9

def player_move(board, tick):
    print('PLAYER TURN!')

    try:
        move = int(input('Choose position for your tick (int in range from 1 to 9): '))
    except ValueError:
        print('Pass an integer, please!')
        return False

    if (move < 1) or (move > 9):
        print('Number is out of range! Pass a number from range 1 to 9, please.')
        return False
    elif is_square_empty(board, move) is False:
        print('Square is not empty! Try again!')
        return False
    elif not isinstance(move, int):
        print('Pass an integer, please!')
        return False
    else:
        board[move - 1] = tick
        return True

def comp_choice(board):
    """ possible_moves variable contains indexes NOT VALUES! """
    possible_moves = [index for index, value in enumerate(board) if value != 'X' and value != 'O']

    ''' 1. Check if there is a win or a win-block possible in the next turn '''
    for tick in ['O', 'X']:
        for x in possible_moves:
            board_copy = board.copy()
            board_copy[x] = tick
            if is_win(board_copy):
                return x

    ''' 2. Check if center is available (index=4, value=5)'''
    if 4 in possible_moves:
        return 4

    ''' 3. Check if there are corners available '''
    corners_possible = [index for index, value in enumerate(board) if value in [1, 3, 7, 9]]
    if len(corners_possible) > 0:
        return random.choice(corners_possible)

    ''' 4. Check the edges '''
    edges_possible = [index for index, value in enumerate(board) if value in [2, 4, 6, 8]]
    if len(edges_possible) > 0:
        return random.choice(edges_possible)

def comp_move(button, board):
    index = comp_choice(board)
    board[index] = 'O'
    button['text'] = 'O'
    button['state'] = 'disabled'
    print('Computer place "O" on square {}:'.format(index + 1))
    print_board(board)

def is_win(board):
    return (len(set([board[x] for x in [0, 1, 2]])) == 1 or
            len(set([board[x] for x in [3, 4, 5]])) == 1 or
            len(set([board[x] for x in [6, 7, 8]])) == 1 or
            len(set([board[x] for x in [0, 3, 6]])) == 1 or
            len(set([board[x] for x in [1, 4, 7]])) == 1 or
            len(set([board[x] for x in [2, 5, 8]])) == 1 or
            len(set([board[x] for x in [0, 4, 8]])) == 1 or
            len(set([board[x] for x in [2, 4, 6]])) == 1)

def is_game_finished(board, score):
    if is_win(board):
        end_message(score)
        return True
    if is_board_full(board):
        end_message(0)
        return True
    return False

def new_game(buttons):
    x = input('Do You want to play again? ["y" to play]: ')
    if x == 'y':
        restart(buttons)

def click(button, index, board):
    button['text'] = 'X'
    button['state'] = 'disabled'
    button['disabledforeground'] = 'black'
    board[index] = 'X'

    comp_move(board, button)

def restart(buttons, board):
    for index, value in enumerate(buttons):
        value['state'] = 'normal'
        value['text'] = str(index + 1)
    board = [x for x in range(1, 10)]

def game():
    board = [x for x in range(1, 10)]
    #welcome_message()

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.title('Tic Tac Toe')
    window.geometry('617x700')
    frame = tk.Frame(window, bg='#4d94ff')
    frame.place(height=700, width=617)

    config = ['#2b6fd4', 5, 10, 27]

    button1 = tk.Button(frame, text='1', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button1, 0, board))
    button2 = tk.Button(frame, text='2', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button2, 1, board))
    button3 = tk.Button(frame, text='3', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button3, 2, board))
    button4 = tk.Button(frame, text='4', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button4, 3, board))
    button5 = tk.Button(frame, text='5', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button5, 4, board))
    button6 = tk.Button(frame, text='6', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button6, 5, board))
    button7 = tk.Button(frame, text='7', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button7, 6, board))
    button8 = tk.Button(frame, text='8', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button8, 7, board))
    button9 = tk.Button(frame, text='9', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], command=lambda: click(button9, 8, board))
    restart_button = tk.Button(frame, text='Restart game', fg='black', bg='white', height=5, width=27, bd=5, command=lambda: restart(buttons, board))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    restart_button.grid(row=3, column=1)

    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    window.mainloop()


    control = False
    while True:
        ''' Player 1 '''
        while control is False:
            control = player_move(board, 'X')
            if control is True:
                print_board(board)
        if is_game_finished(board, 1):
            break
        control = False

        ''' Computer '''
        comp_move(board, buttons)
        if is_game_finished(board, 2):
            break

    new_game(buttons)


if __name__ == '__main__':
    game()