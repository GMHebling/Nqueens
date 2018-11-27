from random import randint
N = 4
#Criado em 27/11
#Problema das N rainhas

#Representacao LAGUNA: board = [c1, c2, c3, c4]
#linha i => coluna board[i]


def create_board(n):
	#cria um posicionamento ordenado de rainhas num tabuleiro de dimensao n
	board = []
	for index in range(n):
		board.append(index)
	return board

def shuffle_board(board, n):
	#realiza n permutacoes nas posicoes das rainhas
	for index in range(n):
		new_index = randint(0,n-1)
		old_value = board[index]
		board[index] = board[new_index]
		board[new_index] = old_value
	return board	

def positive_diagonal(board):
	n = len(board)
	pos_diag = []
	for index in range(n):
		value = index - board[index]
		pos_diag.append(value)

	return pos_diag

def negative_diagonal(board):
	n = len(board)
	neg_diag = []
	for index in range(n):
		value = index + board[index]
		neg_diag.append(value)
	return neg_diag

new_board = create_board(N)
new_board = shuffle_board(new_board, N)

