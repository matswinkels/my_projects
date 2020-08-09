""" Tic Tac Toe - two players version """

def welcome_message():
    print('\n\nWELCOME TO THE TIC TAC TOE GAME!')
    print(1,2,3)
    print(4,5,6)
    print(7,8,9)
    print()

def end_message(score):
    if score == 0:
        print("IT'S A TIE!")
    else:
        print('CONGRATULATIONS PLAYER {}. YOU WIN!'.format(score))

def print_board(board):
    print(*[board[x] for x in range(3)], sep='   ', end='\n\n')
    print(*[board[x] for x in range(3, 6)], sep='   ', end='\n\n')
    print(*[board[x] for x in range(6, 9)], sep='   ', end='\n\n')

def is_board_empty(board):
    return board.count('X') == 0 and board.count('O') == 0

def is_square_empty(board, move):
    return board[move - 1] != 'X' and board[move - 1] != 'O'

def is_board_full(board):
    return board.count('X') + board.count('O') == 9

def player_move(board, tick):
    if tick == 'X':
        print('PLAYER 1 (X) TURN!')
    else:
        print('PLAYER 2 (O) TURN!')

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

def restart():
    x = input('Do You want to play again? ["y" to play]: ')
    if x == 'y':
        game()

def game():
    board = [x for x in range(1, 10)]
    welcome_message()
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

        ''' Player 2 '''
        while control is False:
            control = player_move(board, 'O')
            if control is True:
                print_board(board)
        if is_game_finished(board, 2):
            break
        control = False

    restart()


if __name__ == '__main__':
    game()




