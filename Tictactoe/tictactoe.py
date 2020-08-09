import random
import tkinter as tk

def is_square_empty(board, move):
    return board[move - 1] != 'X' and board[move - 1] != 'O'

def is_board_full(board):
    return board.count('X') + board.count('O') == 9

def is_win(board):
    return (len(set([board[x] for x in [0, 1, 2]])) == 1 or
            len(set([board[x] for x in [3, 4, 5]])) == 1 or
            len(set([board[x] for x in [6, 7, 8]])) == 1 or
            len(set([board[x] for x in [0, 3, 6]])) == 1 or
            len(set([board[x] for x in [1, 4, 7]])) == 1 or
            len(set([board[x] for x in [2, 5, 8]])) == 1 or
            len(set([board[x] for x in [0, 4, 8]])) == 1 or
            len(set([board[x] for x in [2, 4, 6]])) == 1)

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

def click(button, index, board, buttons):
    board[index] = 'X'
    button['text'] = 'X'
    button['state'] = 'disabled'
    button['disabledforeground'] = 'black'

    if is_win(board):
        game_end(buttons, 1)
    elif is_board_full(board):
        game_end(buttons, 0)
    else:
        comp_move(board, buttons)

def comp_move(board, buttons):
    index = comp_choice(board)
    board[index] = 'O'
    buttons[index]['text'] = 'O'
    buttons[index]['state'] = 'disabled'
    buttons[index]['disabledforeground'] = 'black'

    if is_win(board):
        game_end(buttons, 2)

    if is_board_full(board):
        game_end(buttons, 0)

def game_end(buttons, score):
    for b in buttons:
        b['state'] = 'disabled'
        b['disabledforeground'] = 'black'
    if score == 0:
        result['text'] = 'IT IS A TIE. TRY AGAIN.'
        result.grid(row=4, column=1)
    elif score == 1:
        result['text'] = 'PLAYER WINS!'
        result.grid(row=4, column=1)
    else:
        result['text'] = 'COMPUTER WINS!'
        result.grid(row=4, column=1)

def game():
    board = [x for x in range(1, 10)]
    result['text'] = ' '
    config = ['#2b6fd4', 5, 6, 13]
    font = ('Arial', 18)

    button1 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button1, 0, board, buttons))
    button2 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button2, 1, board, buttons))
    button3 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button3, 2, board, buttons))
    button4 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button4, 3, board, buttons))
    button5 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button5, 4, board, buttons))
    button6 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button6, 5, board, buttons))
    button7 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button7, 6, board, buttons))
    button8 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button8, 7, board, buttons))
    button9 = tk.Button(frame, text=' ', bg=config[0], bd=config[1], activebackground='#c0d4f2', height=config[2], width=config[3], font=font, command=lambda: click(button9, 8, board, buttons))
    restart_button = tk.Button(frame, text='Restart game', fg='black', bg='white', height=5, width=27, bd=5, command=lambda: game())

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


if __name__ == '__main__':
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.title('Tic Tac Toe')
    window.geometry('602x700')
    frame = tk.Frame(window, bg='#4d94ff')
    frame.place(height=700, width=602)
    result = tk.Label(frame, text=' ', bg='#4d94ff', font=('Arial', 12))

    game()
