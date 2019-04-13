'''
Created on Nov 7, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    ''' returns a 2d array of all live cells - with the value 
    of 1 - except for a one-cell-wide border of empty cells'''
    A=createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0:
                A[row][col]=0
            elif row==(h-1) or col==(w-1):
                A[row][col]=0
            else:
                A[row][col]=1
    return A

def randomCells(w,h):
    '''returns an array of randomly-assigned 1's
    and 0's except that the outer edge of the array is still completely empty'''
    A=createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row==0 or col==0:
                A[row][col]=0
            elif row==(h-1) or col==(w-1):
                A[row][col]=0
            else:
                A[row][col]=random.choice( [0,1] )
    return A

def copy(A):
    '''deep copy of a board'''
    new_board=createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            new_board[row][col]= A[row][col]
    return new_board

def innerReverse(A):
    ''' takes an old 2d array (or "generation") and then
    creates a new generation of the same shape and size'''
    reverse_board=copy(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0:
                reverse_board[row][col]=0
            elif row==(len(A)-1) or col==(len(A)-1):
                reverse_board[row][col]=0
            else:
                if reverse_board[row][col]==0:
                    reverse_board[row][col]=1
                elif reverse_board[row][col]==1:
                    reverse_board[row][col]=0
    return reverse_board

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    board=copy(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row==0 or col==0:
                board[row][col]=0
            elif row==(len(A)-1) or col==(len(A)-1):
                board[row][col]=0
            else:
                if countNeighbors(row, col, A)<2:
                    board[row][col]=0
                if countNeighbors(row, col, A)>3:
                    board[row][col]=0
                if countNeighbors(row, col, A)==3:
                    board[row][col]=1
    return board

def countNeighbors( row, col, A ):
    '''returns the number of live neighbors for a cell 
    in the board A at a particular row and col'''
    x=0
    #if A[row][col]==1:
        #x+=1
    if A[row][col+1]==1:
        x+=1
    if A[row][col-1]==1:
        x+=1
    if A[row+1][col]==1:
        x+=1
    if A[row+1][col+1]==1:
        x+=1
    if A[row+1][col-1]==1:
        x+=1
    if A[row-1][col]==1:
        x+=1
    if A[row-1][col+1]==1:
        x+=1
    if A[row-1][col-1]==1:
        x+=1
    return x

A = [ [0,0,0,0,0],[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0],[0,0,0,0,0]]
print(printBoard(A))
A2 = next_life_generation( A )
print(printBoard(A2))
A3 = next_life_generation( A2 )
print(printBoard(A3))

#A=randomCells(8,8)
#print(printBoard(A))
#A2=innerReverse(A)
#print(printBoard(A2))

# oldA=createBoard(2, 2)
# print(printBoard(oldA))
# newA=copy(oldA)
# print(printBoard(newA))
# oldA[0][0]=1
# print(printBoard(oldA))
# print(printBoard(newA))

#print(printBoard(randomCells(10,10)))
#print(printBoard(innerCells(5, 5)))
#print(diagonalize(7, 6))
#print(printBoard(diagonalize(7,6)))