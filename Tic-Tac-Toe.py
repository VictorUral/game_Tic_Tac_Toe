# Tic-Tac-Toe
from random import choice

def draw_board (board:list):
	''' Вывод игровой доски '''
	print()
	k = 2
	for i in range(3):
		print (" ", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
		if k:
			print (' ' + "-" * 11)
			k -= 1
			
def display_XO_board (board:list, XO:str):
	''' Принимает список с нумерацией клеток доски и взависимости от указаной клетки игроком ставит в нее Х или О '''
	while True:
		try:
			num = int(input('\nВведите номер клетки чтобы сделать ход: '))
			if board[num - 1] != 'X' and board[num - 1] != 'O':
				board[num - 1] = XO
				break
			print (f'В эту клетку уже был сделан ход')
		except ValueError:
			print ('Вводите только число клетки, на которую собираитесь сделать ход')
	
def checking_winnings (board:list):
	''' Проверят не сложилась ли выигрышная комбинация '''
	win_comb = [(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8)]
	for w in win_comb:
		if board[w[0]] == board[w[1]] == board[w[2]] == 'X':
			print ('\n\t\tХ выиграли')
			return True
		elif board[w[0]] == board[w[1]] == board[w[2]] == 'O':
			print ('\n\t\tО выиграли')
			return True
	return False
	
def repeat_game ():
	''' Перезапуск игры '''
	R = input (f'\nВведите R чтобы играть еще ').upper ()
	if R != 'R':
		print (f'\n\t\tСпасибо за игру')
		return True
	else:
		return False

def main ():
	XO = choice ('XO') # случайный выбор, кто будет ходить первым крестики или нолики
	print (f'Вас приветствует игра крестики-нолики. Первыми будут ходить - {XO}')
	for x in range (9):
		display_XO_board (board, XO)
		draw_board (board)
		if XO == 'X':
			XO = 'O'
		else:
			XO = 'X'
		if x >= 4:
			win = checking_winnings (board)
			if win:
				break
	else:
		print ('\n\t\tНичья')

while True:
	board = [x for x in range (1, 10)]
	main ()
	r = repeat_game ()
	if r:
		break
