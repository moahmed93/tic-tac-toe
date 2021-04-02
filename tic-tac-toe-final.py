


def display(board): 

    print("     |     |     ")
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print("     |     |     ")
    print("-----|-----|-----")   
    print("     |     |     ")
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print("     |     |     ")
    print("-----|-----|-----")    
    print("     |     |     ")
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print("     |     |     ")

test_board = ['0','1','2','3','4','5','6','7','8','9']

display(test_board)
print("Welcome to Tic Tac Toe!")


def clear():
    print("\n"*10)

def player_marker():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O?" ).upper()

    if marker == 'O':
        print("\nPlayer 1 is O, Player 2 is X")
        return ('O','X')
        
    else: 
        
        print("\nPlayer 1 is X, Player 2 is O")
        return('X','O')

new_board = ['0','1','2','3','4','5','6','7','8','9']
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{player} - Choose your next position: (1-9, Top left is 1, bottom right is 9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')



def place_marker(theboard, marker, position):
    theboard[position] = marker

def check_win(board,mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # TOP ROW BINGO
    (board[4] == mark and board[5] == mark and board[6] == mark) or # MIDDLE ROW BINGO
    (board[7] == mark and board[8] == mark and board[9] == mark) or # BOTTOM ROW BINGO
    (board[7] == mark and board[4] == mark and board[1] == mark) or # VERTICAL LEFT
    (board[8] == mark and board[5] == mark and board[2] == mark) or # VERTICAL MIDDLE
    (board[9] == mark and board[6] == mark and board[3] == mark) or # VERTICAL RIGHT
    (board[9] == mark and board[5] == mark and board[1] == mark) or # DIAGONAL BACKWARD SLASH
    (board[7] == mark and board[5] == mark and board[3] == mark)) # DIAGONAL FORWARD SLASH

while True:
    # Reset the board
    theboard = [' '] * 10
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Y or N:')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # FUNCS FOR P1's TURN
            clear()
            display(theboard)
            position = player_choice(theboard, "Player 1")
            place_marker(theboard, player1_marker, position)

            if check_win(theboard, player1_marker):
                clear()
                display(theboard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    clear()
                    display(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # FUNCS FOR P2's TURN
            clear()
            display(theboard)
            position = player_choice(theboard, "Player 2")
            place_marker(theboard, player2_marker, position)

            if check_win(theboard, player2_marker):
                clear()
                display(theboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theboard):
                    clear()
                    display(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
