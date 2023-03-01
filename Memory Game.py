# Players determine size of the board (maximum 9x9)
# If the board has an odd number of cells, the last cell is designated as an unused cell
# An unused cell is shown with "@", the rest are shown as "?"
# The game board has randomly generated pairs of letters
# Players take turn to pick two cells
# Show the letter of the cell when picked
# If the player choses two non-matching letters, letters are hidden again and next player plays
# If the player chooses two matching letters, letters stay visible and same player picks again
# If the player gives an invalid cell (unused/outside the board), he loses the turn
# When all cells are opened, the game is over 
# Show scores and winner(s)


import random
def even_check(rows,cols):
    even = (rows*cols) % 2 #check for odd
    return even

#function to create the answer board
def answer_game(rows, cols, even):
    num = int((rows*cols - even )/2) # number of letters to create
    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    letterlist = [] #list of letters used
    for i in range(num):
        letter = random.choice(letters)
        letterlist.append(letter) # adding letter to list
        letters.remove(letter) #removing letter from original list to prevent duplicates
    letterlist = letterlist *2
    random.shuffle(letterlist) # shuffling letters

    #printing letter list into nested list based on rows and cols
    answer = [] 
    for i in range(rows):
        column = letterlist[:cols]
        letterlist = letterlist[cols:]
        answer.append(column)
    return answer
            
#function to create the player board
def board_game(rows,cols,even):
    board = []
    for i in range(rows):
        column = ["?"] * cols
        board.append(column)
    if even == 1:
        board[rows-1][cols-1] = "@"
    return board

#function to check for the valid inputs
def checker(x,y,rows,cols,board):
    valid = False
    
    if x < 0 or x >= rows or y < 0 or y >= cols:
        print("Invalid coordinates! You lose your turn.")
    elif board[x][y] == '@':
        print("You cannot select the unused cell! You lose your turn.")
    elif board[x][y] != '?':
        print("You cannot select a visible cell! You lose your turn.")
    else:
        valid = True
    return valid

#function to output the boards
def print_board(board):
    print(" ",end=" ")
    for i in range(len(board[0])):
        print(i, end=' ')
    print()
    for j in range(len(board)):
        print(j, end= ' ')
        for cell in board[j]:
            print(cell, end=' ')
        print()
    print()

#main function
def start():
    rows = int(input("Enter number of rows (1-9): "))
    cols = int(input("Enter number of columns (1-9): "))
    even = even_check(rows,cols)
    answer = answer_game(rows, cols, even)
    board = board_game(rows,cols,even)
    
    players = []
    scores = {}
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input("Enter player name: ")
        players.append(name)
        scores[name] = 0
    current_player = 0

    print("***************** CHEAT **************************")
    print_board(answer)
    print("***************** CHEAT **************************")
    
    while True:
        print("Current player:", players[current_player])
        print_board(board)
        try:
            #Player 1st Input
            x1, y1 = map(int, input("Enter the coordinates of the first cell (x y): ").split())
            if checker(x1,y1,rows,cols,board) == False:
                current_player = (current_player + 1) % num_players
                continue
    
            #Create a temporary board to display first choice
            temp_board = [ele[:] for ele in board]
            temp_board[x1][y1] = answer[x1][y1]
            print_board(temp_board)
            
            #Player 2nd input
            x2, y2 = map(int, input("Enter the coordinates of the second cell (x y): ").split())
            if checker(x2,y2,rows,cols,board) == False:
                current_player = (current_player + 1) % num_players
                continue
            #display 2nd choice
            temp_board[x2][y2] = answer[x2][y2]
            print_board(temp_board)
            
            #Check if letters are matching
            if answer[x1][y1] == answer[x2][y2]:
                print("Matched pair! You get a point.")
                
                #give player a point
                scores[players[current_player]] += 1
                
                #set the board
                board[x1][y1] = answer[x1][y1]
                board[x2][y2] = answer[x1][y1]
                
                #check if the game is over
                game_over = True
                for row in board:
                    if '?' in row:
                        game_over = False
                        break
                if game_over:
                    print("Game over!")
                    
                    #display scores and winner(s)
                    for player in scores:
                        print(player, scores[player])
                    max_score = max(scores.values())
                    winners = [player for player in scores if scores[player] == max_score]
                    if len(winners) > 1:
                        print("There is a tie between: ", winners)
                    else:
                        print("The winner is: ", winners[0])
                        break
            else:
                #move on to the next player
                print("Non-matching pair! You lose your turn.")
                current_player = (current_player + 1) % num_players

        except ValueError:
            print("Invalid coordinates")

start()