import random

class ConnectFour:
    
    def __init__(self):
        self.board = []
        self.playable = [7] * 8
        for hole in range(8):
            self.board.append([" "] * 8)
            
    def __str__(self):
        for row in range(8):
            rowString = ""
            for piece in range(8):
                rowString += self.board[row][piece]
                if piece != 7:
                    rowString += "|"
            print(rowString)
            if row != 7:
                print("-" * 15)
        print("0 1 2 3 4 5 6 7")
        return ""
    
    def playMove(self, column, playerNum):
        if self.playable[column] == -1:
            return False
        elif playerNum == 1:
            self.board[self.playable[column]][column] = "X"
            self.playable[column] -= 1
            return True
        else:
            self.board[self.playable[column]][column] = "+"
            self.playable[column] -= 1
            return True
    
    def isFourRow(self, row, player):
        if player == 1:
            pieceType = "X"
        else:
            pieceType = "+"
        for possibleFour in range(5):
            currentRow = True
            for holeValue in range(4):
                if self.board[row][possibleFour + holeValue] != pieceType:
                    currentRow = False
            if currentRow:
                return True
        return False
        
    def isFourColumn(self, column, player):
        if player == 1:
            pieceType = "X"
        else:
            pieceType = "+"
        for possibleFour in range(5):
            currentColumn = True
            for holeValue in range(4):
                if self.board[possibleFour + holeValue][column] != pieceType:
                    currentColumn = False
            if currentColumn:
                return True
        return False
    
    def isDownRightDiagonal(self, player):
        if player == 1:
            pieceType = "X"
        else:
            pieceType = "+"
        for startColumn in range(5):
            for startRow in range(5):
                currentDiagonal = True
                for holeValue in range(4):
                   if self.board[startRow + holeValue][startColumn + holeValue] != pieceType:
                       currentDiagonal = False
                if currentDiagonal:
                    return True
        return False
    
    def isUpRightDiagonal(self, player):
        if player == 1:
            pieceType = "X"
        else:
            pieceType = "+"
        for startColumn in range(5):
            for startRow in range(3, 8):
                currentDiagonal = True
                for holeValue in range(4):
                    if self.board[startRow - holeValue][startColumn + holeValue] != pieceType:
                        currentDiagonal = False
                if currentDiagonal:
                    return True
        return False
    
    def isWinning(self, player):
        if sum(self.playable) > 52:
            return False
        elif self.isDownRightDiagonal(player):
            return True
        elif self.isUpRightDiagonal(player):
            return True
        else:
            for rowColumn in range(8):
                if self.isFourRow(rowColumn, player):
                    return True
                if self.isFourColumn(rowColumn, player):
                    return True
     
    def scoreCalc(self, player, verbose = False):
        scoreDict = {"Win" : 0, "Lose" : 0, "Win in 1" : 0, "Lose in 1" : 32767, "Win in 2" : 0, "Lose in 2" : 32767, "Win in 3" : 0, "Lose in 3" : 32767}
        if self.isWinning(player):
            scoreDict["Win"] = 1
            return scoreDict["Win"] * (262144 ** 7)
        else:
            scoreDict["Win"] = 0
        if self.isWinning(player - 1):
            scoreDict["Lose"] = 0
        else:
            scoreDict["Lose"] = 1
        for possibleMove in range(8):
            if self.playMove(possibleMove, player):
                if self.isWinning(player):
                    scoreDict["Win in 1"] += 1
                else:
                    for possibleMove2 in range(8):
                        if self.playMove(possibleMove2, player - 1):
                            if self.isWinning(player - 1):
                                scoreDict["Lose in 1"] -= 1
                            else:
                                for possibleMove3 in range(8):
                                    if self.playMove(possibleMove3, player):
                                        if self.isWinning(player):
                                            scoreDict["Win in 2"] += 1
                                        else:
                                            for possibleMove4 in range(8):
                                                if self.playMove(possibleMove4, player - 1):
                                                    if self.isWinning(player - 1):
                                                        scoreDict["Lose in 2"] -= 1
                                                    else:
                                                        for possibleMove5 in range(8):
                                                            if self.playMove(possibleMove5, player):
                                                                if self.isWinning(player):
                                                                    scoreDict["Win in 3"] += 1
                                                                '''else:
                                                                    for possibleMove6 in range(8):
                                                                        if self.playMove(possibleMove6, player - 1):
                                                                            if self.isWinning(player - 1):
                                                                                scoreDict["Lose in 3"] -= 1
                                                                            self.board[self.playable[possibleMove6] + 1][possibleMove6] = " "
                                                                            self.playable[possibleMove6] += 1'''
                                                                self.board[self.playable[possibleMove5] + 1][possibleMove5] = " "
                                                                self.playable[possibleMove5] += 1
                                                    self.board[self.playable[possibleMove4] + 1][possibleMove4] = " "
                                                    self.playable[possibleMove4] += 1
                                        self.board[self.playable[possibleMove3] + 1][possibleMove3] = " "
                                        self.playable[possibleMove3] += 1
                                    if possibleMove3 != 7 and verbose:
                                        print("{0} % done!".format(100 * ((possibleMove)/8 + ((possibleMove2)/64) + ((possibleMove3 + 1)/512))))    
                            self.board[self.playable[possibleMove2] + 1][possibleMove2] = " "
                            self.playable[possibleMove2] += 1
                        if possibleMove2 != 7 and verbose:
                            print("{0} % done!".format(100 * ((possibleMove)/8 + ((possibleMove2 + 1)/64))))
                self.board[self.playable[possibleMove] + 1][possibleMove] = " "
                self.playable[possibleMove] += 1
            print("{0} % done!".format(100 * (1+possibleMove)/8))
        score = scoreDict["Win"] * (262144 ** 7) + scoreDict["Lose"] * (262144 ** 6) + scoreDict["Win in 1"] * (262144 ** 5) + scoreDict["Lose in 1"] * (262144 ** 4) + scoreDict["Win in 2"] * (262144 ** 3) + scoreDict["Lose in 2"] * (262144 ** 2) + scoreDict["Win in 3"] * (262144 ** 1) + scoreDict["Lose in 3"] * (262144 ** 0)
        return score
    
    def distanceFromCenter(self, column):
        row = self.playable[column]
        return ((row - 3.5) ** 2 + (column - 3.5) ** 2) ** (1/2)
    
    def playGame(self):
        print("Welcome to Connect 4!")
        playerNum = int(input("Would you like to be player 1 or 2? "))
        parity = 0
        while not self.isWinning(1) and not self.isWinning(2):
            parity += 1
            if parity % 2 == 2 - playerNum:
                print("Your turn!")
                print(self)
                legalMove = False
                while not legalMove:
                    playerMove = int(input("Choose a column 0-7, with 0 being the leftmost column: "))
                    legalMove = self.playMove(playerMove, playerNum)
            else:
                legalMove = False
                while not legalMove:
                    bestMoveValue = 262144 ** 8
                    bestDistance = 64
                    bestMove = 0
                    for possibleMove in range(8):
                        if self.playMove(possibleMove, playerNum - 1):
                            currentValue = self.scoreCalc(playerNum, True)
                            print("Value of {0} is {1}".format(str(possibleMove), str(currentValue)))
                            if bestMoveValue > currentValue:
                                bestMoveValue = currentValue
                                bestMove = possibleMove
                                bestDistance = self.distanceFromCenter(possibleMove)
                            elif bestMoveValue == currentValue:
                                if bestDistance > self.distanceFromCenter(possibleMove):
                                    bestMoveValue = currentValue
                                    bestMove = possibleMove
                                    bestDistance = self.distanceFromCenter(possibleMove)
                            self.board[self.playable[possibleMove] + 1][possibleMove] = " "
                            self.playable[possibleMove] += 1
                    legalMove = self.playMove(bestMove, playerNum - 1)
                    print("The computer played {0}!".format(bestMove))
        print(self)
        if parity % 2 == 2 - playerNum:
            print("You win!")
        else:
            print("You lose...")
    
    def computerGame(self):
        parity = 0
        while not self.isWinning(1) and not self.isWinning(2):
            parity += 1
            if parity % 2 == 1:
                playerNum = 1
            else:
                playerNum = 2
            legalMove = False
            while not legalMove:
                bestMoveValue = 262144 ** 8
                bestDistance = 64
                bestMove = 0
                for possibleMove in range(8):
                    if self.playMove(possibleMove, playerNum):
                        currentValue = self.scoreCalc(playerNum - 1)
                        print("Value of {0} is {1}".format(str(possibleMove), str(currentValue)))
                        if bestMoveValue > currentValue:
                            bestMoveValue = currentValue
                            bestMove = possibleMove
                            bestDistance = self.distanceFromCenter(possibleMove)
                        elif bestMoveValue == currentValue:
                            if bestDistance > self.distanceFromCenter(possibleMove):
                                bestMoveValue = currentValue
                                bestMove = possibleMove
                                bestDistance = self.distanceFromCenter(possibleMove)
                        self.board[self.playable[possibleMove] + 1][possibleMove] = " "
                        self.playable[possibleMove] += 1
                legalMove = self.playMove(bestMove, playerNum)
                print("The computer player {0} played {1}!".format(playerNum, bestMove))
                print(self)
        if parity % 2 == 1:
            print("Computer player 1 won!")
        else:
            print("Computer player 2 won!")
            
conFour = ConnectFour()
conFour.playGame()