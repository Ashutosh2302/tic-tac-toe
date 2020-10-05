board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

players=[]

def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def game():

    current_player=1
    p1=input('Enter name of player 1 ')
    p2=input('Enter name of player 2 ')
    players.append(p1)
    players.append(p2)
    while True:
      
        display_board() #function to display game board
        print("{}'s turn".format(players[current_player-1]))

        play_game(current_player) #function to play

        if check_result(current_player)=='draw': # function to check if game is finished(win/tie)
            display_board()
            print('Match Tied')
            break
        elif check_result(current_player):
            display_board()
            print("{} won the game".format(players[current_player-1]))
            break

        current_player=set_turn(current_player) #function to change turns

def set_turn(current_player):
    if current_player==1:
        current_player=2
        return current_player
    if current_player==2:
        current_player=1
        return current_player

def check_result(current_player):
    win1= check_rows(current_player)
    win2= check_columns(current_player)
    win3= check_diagonals(current_player)
    if win1==1 or win2==1 or win3==1:
        return 1
    else:
        if check_draw():
            return 'draw'
        return 0
def check_draw():
    if '-' not in board:
        return 1
    else:
        return 0

def check_rows(current_player):
    if current_player==1:
        symbol='X'
    if current_player==2:
        symbol='0'
    win=0
    if board[0]==board[1]==board[2]==symbol or board[3]==board[4]==board[5]==symbol or board[6]==board[7]==board[8]==symbol:
        win=1
    return (win)

def check_columns(current_player):
    if current_player == 1:
        symbol = 'X'
    if current_player == 2:
        symbol = '0'
    win = 0
    if board[0] == board[3] == board[6] == symbol or board[1] == board[4] == board[7] == symbol or board[2] == board[5] == board[8] == symbol:
        win = 1
    return(win)

def check_diagonals(current_player):
    if current_player == 1:
        symbol = 'X'
    if current_player == 2:
        symbol = '0'
    win = 0
    if board[0] == board[4] == board[8] == symbol or board[2] == board[4] == board[6] == symbol:
        win = 1
    return (win)

def play_game(current_player):
    if current_player == 1:
        while True:
            location = int(input(('Enter location to place X '))) - 1
            if board[location] == '-':
                board[location] = 'X'
                break
            else:
                print('Location Busy try another one')
    if current_player == 2:
        while True:
            location = int(input(('Enter location to place 0 '))) - 1
            if board[location] == '-':
                board[location] = '0'
                break
            else:
                print('Location Busy try another one')


game()