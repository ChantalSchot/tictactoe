"""Functions needed:
- printBoard will print the layout of the board
- startingPlayer will randomly determine which player (X or O) will start the game (50% chance)
- gameWon will check whether either of the players has won a game
- boardFull will check whether the board is full without either player winning (thus a draw)
- playerTurn will check which player's turn it is, ask for input and if input is valid, update board and change current player
- spaceFree will check whether there is still space to add new move
- addMove
- gameMain starts the game and includes the steps to cycle through at every start of the turn
    (e.g. check whether someone won, if board is full, ask for player input, etc.)
Player setup: Player X and Player O (0 and 1) against each other (so without AI)
"""

from random import randint #random integer to determine who will start

#Starting variables:
board = [" " for x in range(10)] #Use list comprehension to create a list variable for the board with index 0-9.
currentPlayer = " " #currentPlayer should be empty at the start.
gamesWonX = 0  # nr of times X has won
gamesWonO = 0  # nr of times O has won

def printBoard():
    #Prints the board with same position for the numbers as the numerical keyboard.

    #Index 0 of the board is not used (so board is similar to numpad)
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
    print("-----------------")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
    print("-----------------")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")


def startingPlayer():
    #create a random integer (either 0 or 1) that determines whether X or O will start the game.
    global currentPlayer #created global so it can later be changed by the 'playerTurn' function to change turns
    currentPlayer = randint(0,1)
    if currentPlayer == 0:
        print("Player X will start. \n")
    else:
        print("Player O will start. \n")


def gameWon(letter):
    #returns True when X or O has filled any row, thus when three fields in a row return the same letter
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or #lowest row
        (board[4] == letter and board[5] == letter and board[6] == letter) or #middle row
        (board[7] == letter and board[8] == letter and board[9] == letter) or #upper row
        (board[7] == letter and board[4] == letter and board[1] == letter) or #left column
        (board[8] == letter and board[5] == letter and board[2] == letter) or #middle column
        (board[9] == letter and board[6] == letter and board[3] == letter) or #right column
        (board[7] == letter and board[5] == letter and board[3] == letter) or #diagonal top-left to bottom-right
        (board[9] == letter and board[5] == letter and board[1] == letter) #diagonal top-right to bottom-left
    )


def spaceFree(number):
    #checks and returns 'True' if the chosen space is still free.
    return board[number] == " "


def boardFull(board):
    #Checks whether there are any empty spaces on the board.
    #There is always 1 empty space at index 0! Thus board is not full if count > 1 (2 or more spaces left).
    if board.count(" ") > 1:
        return False
    else:
        return True


def addMove(letter, number):
    #add the letter (X or O) to the board at the given index number.
    board[number] = letter


def playerTurn():
    run = True
    global currentPlayer #set variable to global so it can be adjusted to switch turns
    while run: #keep running this function until set to false (when input is valid)
        inputNumber = input()
        try:
            inputNumber = int(inputNumber) #convert input to integer
            if 0 < inputNumber < 10:
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
        except ValueError: #if no proper input, error message is given
            print("That is not a valid number. Please pick a number between 1-9 (without decimals or letters).")


def gameMain():
    print("\n... Starting a game of Tic Tac Toe!\nFor every turn, enter a number on the board that corresponds to the number on your numerical keyboard (thus bottom left is 1, top right is 9).\nPlayer X and Player O will switch turns. The starting player is randomly chosen.\n")
    startingPlayer() #determine player who starts the game
    printBoard() #print empty board

    #global variables to edit them later (wipe board and add win count):
    global board
    global gamesWonX
    global gamesWonO

    while not boardFull(board): #keep playing as long as the board is not full.

        if not gameWon("X") and not gameWon("O"): #ask for input if none of the players have won
            if currentPlayer == 0: #current player is X
                print("\nPlayer X: please enter your next move (nr 1-9).")
            if currentPlayer == 1: #current player is O
                print("\nPlayer O: please enter your next move (nr 1-9).")
            playerTurn() #run 'playerTurn' to get input and add it to board.
            printBoard() #Print new board.
        elif gameWon("X"):
            print("\n... Player X has won!")
            gamesWonX += 1
            break
        elif gameWon("O"):
            print("\n... Player O has won!")
            gamesWonO += 1
            break

    if boardFull(board):
        print("Tied game!")

    #check if player wants to start again:
    while True:
        playAgain = input("\nPlay again? y/n\n")
        if playAgain.lower() == "y" or playAgain.lower == "yes":
            board = [" " for x in range(10)]
            print("\n--------------- N E W   G A M E ---------------")
            print("\nCurrent standings:\nPlayer X - Player O\n   %s     -    %s" % (gamesWonX, gamesWonO))
            gameMain()
        else:
            print("\nFinal standings:\nPlayer X - Player O\n   %s     -    %s" % (gamesWonX, gamesWonO))
            if gamesWonX > gamesWonO:
                print("Congratulations Player X, you won!")
            elif gamesWonX < gamesWonO:
                print("Congratulations Player O, you won!")
            else:
                print("Good job, both! It was a tie.")
        break

#run the main function to start a game:

gameMain()


"""
When the code is run:
1. printBoard() will print the empty layout of the board
2. startingPlayer() will randomly determine which player (X or O) will start the game (50% chance)
3. boardFull checks if board is not full. WHILE NOT FULL: Repeat following until full:
    a. gameWon used to check whether either of the players won (ends game if that is the case).
    b. playerTurn() is used to ask for current player input.
        Should be integer between 1-9 and positioned in empty space (spaceFree), otherwise "error" message is given and playerTurn() is restarted.
    c. if valid, playerTurn adds the number input to the board (addMove) and changes 'current player' to the opposite player to switch turns.
    d. New board is printed. -> Continue again with a (if board is not full)
4. Once board is full, game is ended with a 'tied game'.
"""



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
