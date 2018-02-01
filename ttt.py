# Draw a board, start with an empty board
# Determine who is player 1 and player 2
# min to winner =5
# Iterating through loop
    # Player 1 makes a move
    # check for winner
    # print the board with updated moves
    # player 2 makes a move
    # check for winner
    # print the board with updated moves

def drawBoard(board):
    pass

# This function will mainly contain the "print" syntax to draw and display the board
# on the screen. The each box will have numbers from 1 to 9 which represents the
# unique key to each box. The player will choose numbers to make a move later on

def whoFirst(x=1):
    pass

# This function will then decide which player (Player1 or Player2) will go first
# If it's the automatic play with the computer, this function will determine whether
# the player or the computer goes first
# Here, I created a parameter with a default value of 1 and the players will get an
# option to choose either 1 or 2 depending on who goes first
# If a player chooses 1, his/her icon will automatically become O and the other player
# will have X as his/her icon

def makeMove(number):
    pass

# This function will require a input of numbers from 1~9 depending on which slot
# the player wants to move on. For example, if a player types 1, he/she will move
# to the bottom left corner box. The number will go all the way from bottom-left
# up to top-right. After each move, this function will also automatically print
# the board, so both players can get an updated information of each other's
# movements

def checkWinner():
    pass

# This function will check for a winner after each move either by a player1 or
# player2. There are total of 8 possible cases to determin a winner, across the top
# across the middle, across the bottom, down the left side, down the middle,
# down the right side and lastly two diagonals. I'm going to define all the possible
# winning cases to see if any of those possible cases was satisfied by one of the
# players


def checkBoardFull():
    pass

# This functino will check whether the board has full 9 movements without one
# player winning the game. If this function turns out to be true, it will automatically
# print "The game is draw" at the end
