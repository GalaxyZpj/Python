from os import system
system('clear')
def printBoard(board):
    print(board[7],'|',board[8],'|',board[9])
    print('-','|','-','|','-')
    print(board[4],'|',board[5],'|',board[6])
    print('-','|','-','|','-')
    print(board[1],'|',board[2],'|',board[3])

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def full_board_check():
    if board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] != ' ':
        print('Tie Game')
        return False
    else:
        return True

def playerInput():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1: Choose X or O: ')
        if player1 is 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    marker = (player1,player2)
    print(f'\n\nPlayer 1: {player1}    Player 2: {player2}')
    return marker

position = 0
def placeMarker(board, marker, position):
    i = True
    def win():
            if board[1] == board[2] == board[3] == ('X' or 'O'):
                return False
            elif board[4] == board[5] == board[6] == ('X' or 'O'):
                return False
            elif board[7] == board[8] == board[9] == ('X' or 'O'):
                return False
            elif board[1] == board[4] == board[7] == ('X' or 'O'):
                return False
            elif board[2] == board[5] == board[8] == ('X' or 'O'):
                return False
            elif board[3] == board[6] == board[9] == ('X' or 'O'):
                return False
            elif board[1] == board[5] == board[9] == ('X' or 'O'):
                return False
            elif board[3] == board[5] == board[7] == ('X' or 'O'):
                return False
            else:
                return True
    while i:
        printBoard(board)
        print('Player 1:')
        position = int(input('Choose where to place your marker: '))
        board[position] = marker[0]
        printBoard(board)
        i = win()
        if not i:
            print('PLAYER 1 WINS!!!')
            break
        print('Player 2:')
        position = int(input('Choose where to place your marker: '))
        board[position] = marker[1]
        printBoard(board)
        i = win()
        if not i:
            print('PLAYER 2 WINS!!!')
            break
        i = full_board_check()
        system('clear')
placeMarker(board,playerInput(),position)
