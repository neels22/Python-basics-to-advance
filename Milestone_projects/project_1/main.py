


# display board
# choose a position 
# updating the board
# game on 
# while loop running all these functions
# 

board = ['1','2','3','4','5','6','7','8','9']


def display_board(board):
    # print('\n')
    print('- - -')
    print( board[0] + '|' + board[1] + '|' + board[2] )
    print('- - -')
    print( board[3] + '|' + board[4] + '|' + board[5] )
    print('- - -')
    print( board[6] + '|' + board[7] + '|' + board[8] )
    print('- - -')
    print('\n')

display_board(board)


def player_choice():



    while True:

        player_1 = input('Player 1 choose your marker: x or o')

        if player_1 not in ['x','o']:
            print('Wrong choice, choose among x or o ')
        else:
            print('player 1 is : '+player_1)
            break

    if player_1 =='x':
        player_2 = 'o'
    else:
        player_2 = 'x'
    print('player 2 is : ' + player_2)
    return (player_1,player_2)



player_1 ,player_2 =   player_choice()



def play_your_move():

    print('\n')
    print('current board state: ')
    display_board(board)

    position = int(input('choose your position: '))
    return position


position = play_your_move()

def place_the_marker(position,player):

    board[position-1] = player
    print('\n')
    print('current board state: ')
    display_board(board)


place_the_marker(position,player_1)



def win_check(board):

    # board=['o','o','x',
    #        'o','o','x',
    #        'x','x','o']
    # print(board)
    
    if board[0]=='x' and board[1] == 'x' and board[2] =='x' or board[3]=='x' and board[4] == 'x' and board[5] =='x' or board[6]=='x' and board[7] == 'x' and board[8] =='x':
        return 'player x wins'
    elif board[0]=='x' and board[3] == 'x' and board[6] =='x' or board[1]=='x' and board[4] == 'x' and board[7] =='x' or board[2]=='x' and board[5] == 'x' and board[8] =='x':
        return 'player x wins'
    elif board[0] =='x' and board[4] =='x' and board[8] =='x' or board[2] =='x' and board[4] =='x' and board[6] =='x':
        return 'player x wins'
    
        
    if board[0]=='o' and board[1] == 'o' and board[2] =='o' or board[3]=='o' and board[4] == 'o' and board[5] =='o' or board[6]=='o' and board[7] == 'o' and board[8] =='o':
        return 'player o wins'
    elif board[0]=='o' and board[3] == 'o' and board[6] =='o' or board[1]=='o' and board[4] == 'o' and board[7] =='o' or board[2]=='o' and board[5] == 'o' and board[8] =='o':
        return 'player o wins'
    elif board[0] =='o' and board[4] =='o' and board[8] =='o' or board[2] =='o' and board[4] =='o' and board[6] =='o':
        return 'player o wins'
    
    
res=win_check(board)
print(res)


