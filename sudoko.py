'''
Jorge Bautista, A.I. 
9 x 9 Sudoko Puzzle Solver (using backtracking technique)
'''
def findEmptyCell(board,pos):
	for i in range(9):
		for j in range(9):
			if(board[i][j] == "0"):
				pos.append(i), pos.append(j)
				return True
	return False

def printBoard(board):
	for i in range(9):
		for j in range(9):
			if(j % 3 == 0 ):
				print("|",end="")
			print(board[i][j], end=" ")
		print("")
		if(i == 2 or i == 5):
			print("-------------------")


def isUnique(x,board,pos):
	for i in range(9): #check that number is not present in the rows
		if(x == int(board[pos[0]][i])):
			return False

	for i in range(9): #check that nuber is not preent in the column
		if(x == int(board[i][pos[1]])):
			return False

	yBlock, xBlock = pos[0] - 2, pos[1] - 2 #check that number is not present in  3x3 block
	yBlock = (0 if yBlock < 1 else 3 if 0 < yBlock < 4 else 6)
	xBlock = (0 if xBlock < 1 else 3 if 0 < xBlock < 4 else 6)
	for i in range(3): 
		for j in range(3):
			if(int(board[i + yBlock][j + xBlock]) == x):
				return False

	return True

def solveBoard(board):
	pos = []
	if(not findEmptyCell(board,pos)):
		return True
	y, x = pos[0],pos[1]

	for i in range(1,10):
		if(isUnique(i,board,pos)):
			board[y][x] = i #choose
			if (solveBoard(board)):
				return True
			board[y][x] = "0" #unchoose
	return False 


def main():
	print("Please type in the filename")
	fileName = input()
	with open(fileName,"r") as sudokoFile:
		sudokoBoard = sudokoFile.read()

	sudokoBoard = [item.split(" ") for item in sudokoBoard.split("\n")]
	if(solveBoard(sudokoBoard)):
		print("sudoko board has been solved")
		printBoard(sudokoBoard)
	else:
		print("Board not solvable")


main()