current_player = ''		
winner = False		
count = 0	
play = True		
player_Name = []
tie = False			

board = { 1 : '1', 2 : '2', 3: '3',4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

def get_player_Name(current_player):
    if current_player == 'A':
        return ['B','O']
    else:
        return ['A','X']
    
    

def print_board():
    print("|---|---|---|")

    print("|" , board[1],"|", board[2] , "|" , board[3]  , "|") 

    print("|-----------|")

    print("|" , board[4] , "|", board[5] , "|" , board[6] , "|") 

    print("|-----------|")

    print("|" , board[7] , "|", board[8] , "|" , board[9] , "|") 

    print("|---|---|---|")

    


def win_game(occupied, player_id):
    if board[1] ==occupied and board[2] == occupied and board[3] ==occupied or \
    board[4] ==occupied and board[5] ==occupied and board[6] ==occupied or \
    board[7] ==occupied and board[8] ==occupied and board[9] ==occupied or \
    board[1] ==occupied and board[4] ==occupied and board[7] ==occupied or \
    board[2] ==occupied and board[5] ==occupied and board[8] ==occupied or \
    board[3] ==occupied and board[6] ==occupied and board[9] ==occupied or \
    board[1] ==occupied and board[5] ==occupied and board[9] ==occupied or \
    board[3] ==occupied and board[5] ==occupied and board[7] ==occupied:

        print_board()
        print("Player", player_id, "wins")
        return True

    else:
        return False


def insert_Slot(slot_number,occupied):
    while board[slot_number] == 'X' or board[slot_number]=='O':
        print("That spot is occupied pick another spot")
        slot_number = int(input())
    board[slot_number] =occupied

def play_again():
    print("Another Game? [y/n]")
    play_again = input()

    if play_again.upper() == 'Y':
        for i in board:
            board[i] = i
        return True
    else:
        print("Thanks for playing, Have a good day")
        return False
    
while play:
    print_board()

    player_Name = get_player_Name(current_player)
    current_player = player_Name[0]
    print("Player {}: Select any slot".format(current_player))
    input_slot = int(input())
    insert_Slot(input_slot, player_Name[1])
    count += 1
    winner = win_game(player_Name[1], current_player)
    if count == 9 and not winner:
        print("Match has drawn")
        tie = True
        print_board()
    if winner or tie:
        play = play_again()
        if play:
            current_player = ''
            count = 0