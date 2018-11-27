from random import randint
N = 4

def create_board(n):
	board.range(n)
	return board

def shuffle_board(board, n):
	for index in range(n):
		new_index = randint(0,n)
		old_value = board[index]
		board[index] = board[new_index]
		board[new_index] = old_value
	return board	
	

