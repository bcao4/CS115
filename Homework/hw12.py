'''
Created on Dec 5, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.
'''

class Board(object):
    def __init__(self, width=7, height=6):
        """This is a constructor for Board objects that (in addition to self) takes two named arguments"""
        self.width = width
        self.height = height
        self.board = self.createBoard()
    
    def createRow(self):
        """returns a single row of a board"""
        row = []
        for col in range(self.width):
            row += ['']
        return row
    
    def createBoard(self):
        """returns a representation of the board given a width and height"""
        self.board = []
        for row in range(self.height):
            self.board += [self.createRow()]
        return self.board
    
    def __str__(self):
        """returns a string (it does not print a string) representing the Board object that calls it"""
        board = ''
        for row in range(self.height):
            if row > 0:
                board += '\n'
            for col in range(self.width):
                if self.board[row][col] == '':
                    board += '| '
                else:
                    board += ('|' + self.board[row][col])
            board += '|'
        board += ('\n' + '-' * 2 * self.width + '\n')
        for i in range(self.width):
            board += (' ' + str(i))
        return board
    
    def allowsMove(self, col):
        """This method should return True if the calling Board object can
        allow a move into column c (because there is space available). It returns False if c does not
        have space available or if it is not a valid column."""
        try:
            int(col)
        except:
            return False
        col = int(col)
        if col in list(range(self.width)):
            if self.board[0][col] == '':
                return True
            else:
                return False
        else:
            return False
    
    def addMove(self, col, ox):
        """This method should add an ox checker, where ox is a variable
        holding a string that is either "X" or "O", into column col. """
        if self.allowsMove(col) == True:
            R = -1
            for row in self.board:
                if row[col] == '':
                    R += 1
                else:
                    break
            self.board[R][col] = ox  
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places alternating checkers in those columns,
        starting with 'X' For example, call b.setBoard('012345') to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self,col): 
        """This method should do the "opposite" of addMove. That is, it should
        remove the top checker from the column col."""
        spot = 0
        for row in range(self.height):
            if self.board[row][col] != ' ':
                spot = row
                break
        self.board[spot][col] = ' '
    
    def vertical(self, ox, curRow, curCol):
        """checks for 4 in a row vertically"""
        count = 0
        while count < 4 and curCol < self.width and self.board[curRow][curCol] == ox:
            count += 1
            curCol += 1
        return count == 4
        
    def horizontal(self, ox, curRow, curCol):
        """checks for 4 in a row horizontally"""
        count = 0
        while count < 4 and curRow < self.height and self.board[curRow][curCol] == ox:
            count += 1
            curRow += 1
        return count == 4
    
    def diagnol(self, ox, curRow, curCol):
        """checks for 4 in a row diagonally"""
        count = 0
        while count < 4 and curRow < self.height and curCol < self.width and self.board[curRow][curCol] == ox:
            count += 1
            curRow += 1
            curCol += 1
        return count == 4
    
    def negDiagnol(self, ox, curRow, curCol):
        """checks for 4 in a row diagonally"""
        count = 0
        while count < 4 and curRow < self.height and curCol >= 0 and self.board[curRow][curCol] == ox:
            count += 1
            curRow += 1
            curCol -= 1
        return count == 4
    
    def winsFor(self, ox):
        """This method should return True if the given checker, 'X' or 'O', held
        in ox, has won the calling Board. It should return False otherwise."""
        for row in range(self.height):
            for col in range(self.width):
                if self.horizontal(ox, row, col) or self.vertical(ox, row, col) or self.diagnol(ox, row, col) or self.negDiagnol(ox, row, col) == ox:
                    return True
        return False
   
    def hostGame(self):
        """This is a method that, when called from a connect four board object, will
        run a loop allowing the user(s) to play a game """
        print("Welcome to Connect Four!")
        player = "O"
        while True:
            if self.winsFor(player):
                print(player + " wins -- Congratulations!")
                print(self)
                break
            player = "X" if player == "O" else "O"
            print(self)
            choice = int(input(player + "'s choice: "))
            if not self.allowsMove(choice):
                print("\n")
                continue
            print("\n")
            self.addMove(choice, player)               

b = Board( 7, 6 )
b.hostGame()
            
            