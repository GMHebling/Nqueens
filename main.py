from random import randint
N = 8
max_iter = 100
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

def check_board(diag_1, diag_2):
	n = len(diag_1)
	var_obj = 0
	for index1 in range(n-1):
		value = diag_1[index1]
		value2 = diag_2[index1]
		for index2 in range(index1+1,n):
			next_value = diag_1[index2]
			next_value2 = diag_2[index2]
			if next_value == value or next_value2 == value2:
				var_obj = var_obj + 1
	return var_obj

def print_board(board):
	string = []
	for index in range(len(board)): string.append("=")
	for index in range(len(board)):
		new_string = string
		new_string[board[index]] = "@"
		print(new_string)
		new_string[board[index]] = "="
		

new_board = create_board(N)
new_board = shuffle_board(new_board, N)

for iter in range(max_iter):
	d1 = positive_diagonal(new_board)
	d2 = negative_diagonal(new_board)
	var =  check_board(d1,d2)
	if var != 0:
		new_board = shuffle_board(new_board,N)
	else:
		break

print("Solution found in {} iterations".format(iter))
print_board(new_board)



