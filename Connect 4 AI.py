"""
Brian Norton
"""

#Imports
import copy
import sys

#Places a piece down in the original game state
def placePiece(player,column):
    if bottomPiece == 0:
        print("Column is full, piece cannot be placed")
        return "blew up"
    else:
        game[bottomPiece[column]][column] = player
        if checkScore(column,game) == 100 or checkScore(column,game) == -100:
            return True
        bottomPiece[column] -= 1
    return False

#Prints the game into the console window
def printGame(state):
    for x in range(0,len(state)):
        for y in range(0,len(state[0])):
            if state[x][y] != 0:
                sys.stdout.write(" "+str(state[x][y])+" ")
            else:
                sys.stdout.write("   ")
        print("")

#Scoring function
def checkScore(column,state):
    row = findEmptyTop(column,state)+1
    player = state[row][column]
    if player == 1:
        opp = 2
    else:
        opp = 1
        
    #Points awarded
    connect = [0,1,7,16,100]
    block = [0,1,4,90]
    
    #Initial scores (0 or 1) of placing a piece down
    down = 1
    downblock = horizontalBlock = downRightBlock = downLeftBlock = 0
    horizontal = downRight = downLeft = 0
    
    
    #New Down scoring
    for x in range(2,5):
        if row <= (6-x):
            if state[row+(x-1)][column] != player and row <= (4-x):
                down = 0
                break
            elif state[row+(x-1)][column] == player:
                down = connect[x]
                if x == 4:
                    return connect[4]
        else:
            break                    
    
    
    #Down - blocking opponent
    if row <= 4:
        if state[row+1][column] == opp:
            if row <= 3:
                if state[row+2][column] == opp:
                    if row <= 2:
                        if state[row+3][column] == opp:
                            downblock = block[3]
                        elif row < 1:
                            downblock = 0
                        else:
                            downblock = block[2]
                    else:
                        downblock = block[2]
                elif row < 2:
                    downblock = 0
                else:
                    downblock = block[1]
            else:
                downblock = block[1]
            
                
    #Horizontal
    #Checks to see if there's enough spots for a connect4 (self = 1 place)
    if column >= 1 and state[row][column-1] != opp:
        if column >= 2 and state[row][column-2] != opp:
            if column >= 3 and state[row][column-3] != opp:
                avail = True
            elif column <= 5 and state[row][column+1] != opp:
                avail = True
            else:
                avail = False
        elif column <= 5 and state[row][column+1] != opp and column <= 4 and state[row][column+2] != opp:
            avail = True
        else:
            avail = False
    elif column <= 5 and state[row][column+1] != opp and column <= 4 and state[row][column+2] != opp and column <= 3 and state[row][column+3] != opp:
        avail = True
    else:
        avail = False
    
    #Horizontal
    #Checks the number of pieces in a straight line
    if avail == True:
        if column >= 1 and state[row][column-1] == player:
            if column >= 2 and state[row][column-2] == player:
                if column >= 3 and state[row][column-3] == player:
                    return connect[4]
                elif column <= 5 and state[row][column+1] == player:
                    return connect[4]
                else:
                    horizontal = connect[3]
            elif column <= 5 and state[row][column+1] == player:
                if column <= 4 and state[row][column+2] == player:
                    return connect[4]
                else:
                    horizontal = connect[3]
            else:
                horizontal = 4
        elif column <= 5 and state[row][column+1] == player:
            if column <= 4 and state[row][column+2] == player:
                if column <= 3 and state[row][column+3] == player:
                    return connect[4]
                else:
                    horizontal = connect[3]               
            else:
                horizontal = connect[2]
        else:
            horizontal = connect[1]
    
    #Horizontal blocking
    if downblock != block[3]:
        if column >= 1 and state[row][column-1] == opp:
            if column >= 2 and state[row][column-2] == opp:
                if column >= 3 and state[row][column-3] == opp:
                    horizontalBlock = block[3]
                else:
                    horizontalBlock = block[2]
            else:
                horizontalBlock = 1
        if column <= 5 and state[row][column+1] == opp:
            if column <= 4 and state[row][column+2] == opp:
                if column <= 3 and state[row][column+3] == opp:
                    horizontalBlock = block[3]
                else:
                    horizontalBlock += block[2]
            else:
                horizontalBlock += block[1]
    
    #Down-left / Up-right
    #Checks to see if there's enough spots for a connect4 (self = 1)
    if row <= 4 and column >= 1 and state[row+1][column-1] != opp:
        if row <= 3 and column >= 2 and state[row+2][column-2] != opp:
            if row <= 2 and column >= 3 and state[row+3][column-3] != opp:
                avail = True
            elif row >= 1 and column <= 5 and state[row-1][column+1] != opp:
                avail = True
            else:
                avail = False
        elif row >= 1 and column <= 5 and state[row-1][column+1] != opp and row >= 2 and column <= 4 and state[row-2][column+2] != opp:
            avail = True
        else:
            avail = False
    elif row >= 1 and column <= 5 and state[row-1][column+1] != opp and row >= 2 and column <= 4 and state[row-2][column+2] != opp and row >= 3 and column <= 3 and state[row-3][column+3] != opp:
        avail = True
    else:
        avail = False
        
    #Down-left / Up-right
    #Checks the number of pieces in a straight line
    if avail == True:
        if row <= 4 and column >= 1 and state[row+1][column-1] == player:
            if row <= 3 and column >= 2 and state[row+2][column-2] == player:
                if row <= 2 and column >= 3 and state[row+3][column-3] == player:
                    return connect[4]
                elif row >= 1 and column <= 5 and state[row-1][column+1] == player:
                    return connect[4]
                else:
                    downLeft = 9
            elif row >= 1 and column <= 5 and state[row-1][column+1] == player:
                if row >= 2 and column <= 4 and state[row-2][column+2] == player:
                    return connect[4]
                else:
                    downLeft = connect[3]
            else:
                downLeft = 4
        elif row >= 1 and column <= 5 and state[row-1][column+1] == player:
            if row >= 2 and column <= 4 and state[row-2][column+2] == player:
                if row >= 3 and column <= 3 and state[row-3][column+3] == player:
                    return connect[4]
                else:
                    downLeft = connect[3]               
            else:
                downLeft = connect[2]
        else:
            downLeft = connect[1]
        
    #Down-left / Up-right 
    #Blocking
    if downblock != block[3] and horizontalBlock != block[3]:
        if row <= 4 and column >= 1 and state[row+1][column-1] == opp:
            if row <= 3 and column >= 2 and state[row+2][column-2] == opp:
                if row <= 2 and column >= 3 and state[row+3][column-3] == opp:
                    downLeftBlock = block[3]
                else:
                    downLeftBlock = block[2]
            else:
                downLeftBlock = block[1]
        if row >= 1 and column <= 5 and state[row-1][column+1] == opp:
            if row >= 2 and column <= 4 and state[row-2][column+2] == opp:
                if row >= 3 and column <= 3 and state[row-3][column+3] == opp:
                    downLeftBlock = block[3]
                else:
                    downLeftBlock += block[2]
            else:
                downLeftBlock += block[1]
        
    #Down Right / Up Left
    #Checks to see if there's enough spots for a connect4 (self = 1)
    if row >= 1 and column >= 1 and state[row-1][column-1] != opp:
        if row >= 2 and column >= 2 and state[row-2][column-2] != opp:
            if row >= 3 and column >= 3 and state[row-3][column-3] != opp:
                avail = True
            elif row <= 4 and column <= 5 and state[row+1][column+1] != opp:
                avail = True
            else:
                avail = False
        elif row <= 4 and column <= 5 and state[row+1][column+1] != opp and row <= 3 and column <= 4 and state[row+2][column+2] != opp:
            avail = True
        else:
            avail = False
    elif row <= 4 and column <= 5 and state[row+1][column+1] != opp and row <= 3 and column <= 4 and state[row+2][column+2] != opp and row <= 2 and column <= 3 and state[row+3][column+3] != opp:
        avail = True
    else:
        avail = False
        
    #Down Right / Up Left
    #Checks the number of pieces in a straight line
    if avail == True:
        if row >= 1 and column >= 1 and state[row-1][column-1] == player:
            if row >= 2 and column >= 2 and state[row-2][column-2] == player:
                if row >= 3 and column >= 3 and state[row-3][column-3] == player:
                    return 100
                elif row <= 4 and column <= 5 and state[row+1][column+1] == player:
                    return connect[4]
                else:
                    downRight = connect[3]
            elif row <= 4 and column <= 5 and state[row+1][column+1] == player:
                if row <= 3 and column <= 4 and state[row+2][column+2] == player:
                    return connect[4]
                else:
                    downRight = connect[3]
            else:
                downRight = connect[2]
        elif row <= 4 and column <= 5 and state[row+1][column+1] == player:
            if row <= 3 and column <= 4 and state[row+2][column+2] == player:
                if row <= 2 and column <= 3 and state[row+3][column+3] == player:
                    return connect[4]
                else:
                    downRight = connect[3]              
            else:
                downRight = connect[2]
        else:
            downRight = connect[1]
        
    #Down Right / Up Left
    #Blocking
    if downblock != block[3] and horizontalBlock != block[3] and downLeftBlock != block[3]:
        if row >= 1 and column >= 1 and state[row-1][column-1] == opp:
            if row >= 2 and column >= 2 and state[row-2][column-2] == opp:
                if row >= 3 and column >= 3 and state[row-3][column-3] == opp:
                    downRightBlock = block[3]
                else:
                    downRightBlock = block[2]
            else:
                downLeftBlock = 1
        if row <= 4 and column <= 5 and state[row+1][column+1] == opp:
            if row <= 3 and column <= 4 and state[row+2][column+2] == opp:
                if row <= 2 and column <= 3 and state[row+3][column+3] == opp:
                    downRightBlock = block[3]
                else:
                    downRightBlock += block[2]
            else:
                downRightBlock += block[1]
    
    #Returning the combined scores
    if downblock == block[3] or horizontalBlock == block[3] or downRightBlock == block[3] or downLeftBlock == block[3]:
        return block[3]
    return down + downblock + horizontal + horizontalBlock + downRight + downRightBlock + downLeft + downLeftBlock
    
            
            
    
                
#Find the maximum choice of the next layer of states - used for the AI
def decisionMax(parentState,numOfLevels,initialState,*limit):
    score = [0,0,0,0,0,0,0]
    player = 2
    scoreMult = 1
    
    for x in range(0,boardWidth):
        if parentState[0][x] == 0: #if column of x is available
            newState = returnState(player,x,copy.deepcopy(parentState))
            check = checkScore(x,newState)
            if check == 100:
                if initialState == True:
                    return x
                else:
                    return 100
            if numOfLevels == 1:
                score[x] = scoreMult * check
            else:
                score[x] = scoreMult * (check + decisionMin(newState,numOfLevels-1,False,False))
        else: #Column unavailable
            score[x] = -100
    if initialState == False:
        return max(score)
    else:
        returnLoc = 0
        returnScore = -100
        for x in range(0,7):
            if score[x] > returnScore:
                returnScore = score[x]
                returnLoc = x
        print(returnLoc)
        return returnLoc
    
#Find the minimum value of the next states - predicts the player's best option
def decisionMin(parentState,numOfLevels,initialState,*limit):
    score = [0,0,0,0,0,0,0]
    player = 1
    scoreMult = -1
    
    for x in range(0,boardWidth):
        if parentState[0][x] == 0: #if column of x is available
            newState = returnState(player,x,copy.deepcopy(parentState))
            check = checkScore(x,newState)
            if check == 90:
                check = 90
            if check == 100:
                if initialState == True:
                    return x
                else:
                    return -100
            if numOfLevels == 1:
                score[x] = scoreMult * check
            else:
                score[x] = scoreMult * (check + decisionMax(newState,numOfLevels-1,False,True))
        else: #Column unavailable
            score[x] = 100
    if initialState == False:
        return min(score)
    else:
        returnLoc = 0
        returnScore = 100
        for x in range(0,7):
            if score[x] < returnScore:
                returnScore = score[x]
                returnLoc = x
        #print(returnLoc)
        return returnLoc
            
    
#State change
def returnState(player,column,state):
    """Returns a game state with a new piece at a position"""
    state[findEmptyTop(column,state)][column] = player
    return state

#Checks if column is available
def availableColumn(column,state):
    if state[0][column]:
        return False
    else:
        return True

#Find the top of a given column
def findEmptyTop(column,state):
    if  state[5][column] == 0:
        return 5
    if state[0][column] != 0:
        return -1
    for x in reversed(range(0,boardHeight)):
        if state[x][column] == 0:
            return x
    

    
#Initializations
boardWidth = 7
boardHeight = 6
game = [[0 for x in range(0,boardWidth)] for x in range(0,boardHeight)]
bottomPiece = [5,5,5,5,5,5,5]
gameEnd = False
numberOfLevels = 2

#Main game loop
while gameEnd == False:
    printGame(game)
    print(" 1--2--3--4--5--6--7")
    inputPiece = 0
    inputPiece = input("Enter a row to place a piece: ")
    while int(inputPiece) < 1 or int(inputPiece) > 7 or availableColumn(int(inputPiece)-1,game) == False:
        inputPiece = input("Enter a row to place a piece (1 through 7): ")
    if placePiece(1,int(inputPiece)-1) == True:
        gameEnd = True
    print("Thinking...")
    print("")
    AIplace = decisionMax(game,numberOfLevels,True,True)
    print("AI places piece in row " + str(int(AIplace)+1))
    if placePiece(2,AIplace) == True:
        gameEnd = True
    for x in range(0,7):
        if availableColumn(x,game):
            continue

#End game
printGame(game)
if gameEnd == True:
    print("Connect 4!")
else:
    print("Game ended. No more possible moves.")


    
    



