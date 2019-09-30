"""Functions needed:
- printBoard will print the layout of the board
- playerStart will randomly determine which player (X or O) will start the game (50% chance)
- gameWon will check whether either of the players has won a game
- boardFull will check whether the board is full without either player winning (thus a draw)
- playerTurn will check which player's turn it is and ask for input
- spaceFree will check whether there is still space to move (not won, board not full)
- addMove will add the player's input letter to the board list and print it with the updated game status
- turnCycle includes the steps to cycle through at every start of the turn (e.g. check whether someone won,
   whether board is full, whose turn it is, ask for player input, etc.)


Player X and Player O against each other (so basically 'player 1' and 'player 2', without AI)
"""

from random import randint #random integer to determine who will start

#Starting variables:
board = [" " for x in range(10)] #Use list comprehension to create a list variable for the board with index 0-9.
currentPlayer = " " #currentPlayer should be empty at the start.

def printBoard():
    #Print the board with same position for the numbers as the numerical keyboard.

    #Index 0 of the board is not used (so board is similar to numpad)
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
    print("-----------------")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
    print("-----------------")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")




def playerStart():
    #create a random integer (either 0 or 1) that determines whether X or O will start the game.
    global currentPlayer
    currentPlayer = randint(0,1)
    if currentPlayer == 0:
        print("Player X will start! \n")
    else:
        print("Player O will start! \n")


def gameWon(letter):
    #returns True when X or O has filled any row, thus when three fields in a row return the same letter
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or #lowest row
        (board[4] == letter and board[5] == letter and board[6] == letter) or #middle row
        (board[7] == letter and board[8] == letter and board[9] == letter) or #upper row
        (board[7] == letter and board[4] == letter and board[1] == letter) or #left column
        (board[8] == letter and board[5] == letter and board[2] == letter) or #middle column
        (board[9] == letter and board[6] == letter and board[3] == letter) or #right column
        (board[7] == letter and board[5] == letter and board[3] == letter) or #diagonal top-left bottom-right
        (board[9] == letter and board[5] == letter and board[1] == letter) #diagonal top-right bottom-left
    )

def spaceFree(number):
    #return 'true' if the space is still free.
    return board[number] == " "


def boardFull(board):
    #Checks whether there are still empty spaces on the board.
    #There is always 1 empty space at index 0! Thus board is not full if count > 1.
    if board.count(" ") > 1:
        return False
    else:
        return True


def addMove(letter,number):
    #add the letter (X or O) to the board at the given index number.
    board[number] = letter

def playerTurn():
    run = True
    global currentPlayer
    while run:
        #ask for input and convert to integer.
        inputNumber = input()
        try:
            inputNumber = int(inputNumber)
            if 0 < inputNumber < 10: #integer should be any nr between (including) 1-9
                if spaceFree(inputNumber):
                    if currentPlayer == 0:
                        run = False
                        addMove("X", inputNumber)
                        currentPlayer = 1
                    elif currentPlayer == 1:
                        run = False
                        addMove("O", inputNumber)
                        currentPlayer = 0
                else:
                    print("That space is not empty.")
            else:
                raise ValueError
        except ValueError:
            print("That is not a valid number. Please pick a number between 1-9 (without decimals or letters).")

# def playerTurnO():
#     run = True
#     global currentPlayer
#     while run:
#         #ask for input and convert to integer.
#         inputNumber = input("Please pick your next space. (nr 1-9)")
#         try:
#             inputNumber = int(inputNumber)
#             if 0 < inputNumber < 10: #integer should be any nr between (including) 1-9
#                 if spaceFree(inputNumber):
#                     run = False
#                     addMove("O", inputNumber)
#                     currentPlayer = "X"
#                 else:
#                     print("That space is not empty.")
#             else:
#                 raise ValueError
#         except ValueError:
#             print("That is not a valid number. Please pick a number between 1-9 (without decimals or letters).")

def gameMain():
    print("\n    Starting a game of Tic Tac Toe!\nFor every turn, enter a number on the board that corresponds to the number on your numerical keyboard (thus bottom left is 1, top right is 9).\n")
    playerStart()
    printBoard()
    while not boardFull(board): #keep playing as long as the board is not full.

        if not gameWon("X") and not gameWon("O"): #if none of the players have won:
            if currentPlayer == 0:
                print("\n Player X: please pick your next space. (between nr 1-9)") #notify Player X of their turn.
            if currentPlayer == 1:
                print("\n Player O: please pick your next space. (between nr 1-9)") #Notify Player O of their turn.
            playerTurn() #run 'playerTurn' to get input and add it to board.
            printBoard() #Print new board.
        elif gameWon("X"):
            print("\n Player X has won! Re-run the code to start again.")
            break
        elif gameWon("O"):
            print("\n Player O has won! Re-run the code to start again.")
            break

    if boardFull(board):
        print("Tied game! Re-run the code to start again.")


gameMain()



"""When the code is run:
1. printBoard will print the empty layout of the board
2. playerStart will randomly determine which player (X or O) will start the game (50% chance)
3. boardFull checks if board is not full. IF NOT: Repeat following until full
    a. gameWon used to check whether either of the players won.
    b. playerTurn is used to ask for player input.
        Should be integer between 1-9 in empty space, otherwise "error" message is given and playerTurn is restarted.
    c. playerTurn adds the number input to the board and changes 'current player' to change turns.
    d. Board is printed and next player is notified of their turn.
4. If board is full, game is ended with a 'tied game'.
    
    
    
- gameWon will check whether either of the players has won a game
- boardFull will check whether the board is full without either player winning (thus a draw)
- playerTurn will check which player's turn it is and ask for input
- spaceFree will check whether there is still space to move (not won, board not full)
- addMove will add the player's input letter to the board list and print it with the updated game status
- turnCycle includes the steps to cycle through at every start of the turn (e.g. check whether someone won,
   whether board is full, whose turn it is, ask for player input, etc.)"""



# #testing functions:
# addMove("O",1)
# # addMove("O",2)
# addMove("X",3)
# addMove("O",4)
# # addMove("O",5)
# addMove("X",6)
# addMove("O",7)
# # addMove("O",8)
# playerStart()
# addMove(currentPlayer,5)
# printBoard()
# print("is Space 2 free?", spaceFree(2))
# print("Has player X won?", gameWon("X"))
# print("Has player O won?", gameWon("O"))
# print("Is the board full?", boardFull(board))
