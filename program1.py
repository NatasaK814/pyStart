
import random

#row=[small ring, medium ring, big ring]
#if 1 = exists, else 0 = not exist
row1 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
row2 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
row3 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
table = [row1, row2, row3]

#placements is the move counter, while stats holds the total moves of each game
placements = int(0)
stats = []

#function for the next move
def nextMove():
    row=random.randint(0,2)
    cell=random.randint(0,2)
    ring=random.randint(0,2)
    if (table[row][cell][ring] == 0):
        table[row][cell][ring] = 1
    else:
        nextMove()

#These funtions check all the possible outcomes to see if a game victory occured
def first_row():
    matrix = [table[0][0] , table[0][1], table[0][2]]  #We make a table of the line we want to check
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1): #we check for similar rings
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1): # we check from small -> big ring
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1): # we check from big -> small ring
        finish = True
    else:
        return False
    return True
    
def second_row():
    matrix = [table[1][0] , table[1][1], table[1][2]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True

def third_row():
    matrix = [table[2][0] , table[2][1], table[2][2]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True


def first_collumn():
    matrix = [table[0][0] , table[1][0], table[2][0]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True
    
def second_collumn():
    matrix = [table[0][1] , table[1][1], table[2][1]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True

def third_collumn():
    matrix = [table[0][2] , table[1][2], table[2][2]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True

def Diagonal_right_left():
    matrix = [table[2][0] , table[1][1], table[0][2]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True
        

def Diagonal_left_right():
    matrix = [table[0][0] , table[1][1], table[2][2]]
    finish = False
    if(matrix[0][0] == 1 and matrix[1][0] ==1 and matrix[2][0] == 1):
        finish = True
    elif(matrix[0][1] == 1 and matrix[1][1] ==1 and matrix[2][1] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][2] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][0] == 1 and matrix[1][1] ==1 and matrix[2][2] == 1):
        finish = True
    elif(matrix[0][2] == 1 and matrix[1][1] ==1 and matrix[2][0] == 1):
        finish = True
    else:
        return False
    return True


def check_Diagonal():
    return Diagonal_left_right() or Diagonal_right_left()

def check_rows():
    return first_row() or second_row() or third_row()

def check_collumns():
    return first_collumn() or second_collumn() or third_collumn()

#this funtion analyze the results from the previous functions
def checkVictory():
    diagonal = check_Diagonal() 
    rows = check_rows() 
    collumns = check_collumns() 
    result = diagonal or rows or collumns
    if result: # Victory!
        stats.append(placements) # Save the move Counter
        return True
    else: #Continue playing
        return False 

#We play the game for 100 times
for i in range (0,100):
    #We re-initialize our values
    placements = 0
    row1 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
    row2 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
    row3 = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
    table = [row1, row2, row3]
    #While loop until game victory occurs
    while (not checkVictory()):
        placements += 1
        nextMove()
    #Print when the game finished
    print(table)
    print("Play ", i + 1 , " finished after ", placements , " moves! \n")

#Get the average moves to finish a game
totalMoves = 0
for plays in stats:
    totalMoves += plays

averageMoves = totalMoves/100

print("The average moves number to finish a game was: ", averageMoves, " moves")
