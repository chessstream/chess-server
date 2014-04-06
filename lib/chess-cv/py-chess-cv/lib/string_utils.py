import numpy as np
import game
from functools import reduce

def board_string_to_location_array(board):
	"""A board string is a python list of 8 strings of 8 characters
	"""
	return np.array([[_char_to_location(board[line][c], c, line) 
		for c in range(len(board[line]))] 
		for line in range(len(board))] )

def _char_to_location(c, x, y):
	if ord(c) in range(ord('a'), ord('z') + 1):
		color = 'B'
	else:
		color = 'W'
	if c == '_':
		c = None
	return game.Location(x, y, c, color)

def compare_square_array_to_location_array(squares, locations):
	disappeared, appeared = None, None
	for row in range(len(locations)):
		for col in range(len(locations[row])):
			if locations[row][col].piece and not squares[row][col].has_piece:
				disappeared = (row, col)
			elif squares[row][col].has_piece and not locations[row][col].piece:
				appeared = (row, col)
			elif squares[row][col].has_piece and locations[row][col].piece \
					and squares[row][col].piece_color != \
						locations[row][col].color:
				taken = (row, col)

	return disappeared, appeared, taken

def update_location_array(locations, squares, disappeared, appeared, taken):
	"""Destructive: changes locations in place.
	appeared, disappeared, taken are (row, col), not (x, y)"""
	piece = locations[disappeared[0]][disappeared[1]].piece
	color = locations[disappeared[0]][disappeared[1]].color
	locations[disappeared[0]][disappeared[1]].piece = None
	locations[disappeared[0]][disappeared[1]].color = None
	if not appeared:
		# A piece was taken
		locations[taken[0]][taken[1]].piece = piece
		locations[taken[0]][taken[1]].color = color
	else:
		# Generic move
		locations[appeared[0]][appeared[1]].piece = piece
		locations[appeared[0]][appeared[1]].color = color
		

def location_array_to_board_string(locations):
	board = [['_' for _ in range(8)] for _ in range(8)]
	for row in range(len(locations)):
		for col in range(len(locations[row])):
			if locations[row][col].piece:
				board[row][col] = locations[row][col].piece
	for row in range(len(board)):
		board[row] = reduce(lambda a, b: a + b, board[row])
	return board

def board_string_to_fen(board, rotation, color_to_move):
	if rotation:
		board = _rotate_board_string(board, rotation)
	fen = ''
	for row in board:
		col = 0
		while col < len(row):
			if row[col] != '_':
				fen += row[col]
				col += 1
			else:
				num_empty_squares = 0
				while col < len(row) and row[col] == '_':
					col += 1
					num_empty_squares += 1
				fen += str(num_empty_squares)
		fen += '/'
	fen = fen[:-1]
	fen += ' ' + color_to_move.lower() + " KQkq - 0 1"
	return fen

def _rotate_board_string(board, rotation):
	rotated = board[:]
	for row in range(len(rotated)):
		rotated[row] = ['_' for _ in range(len(rotated[row]))]
	if rotation == 180:
		rotated = _rotate_board_string(_rotate_board_string(board, 90), 90)
	elif rotation == 90:
		for row in range(len(rotated)):
			for col in range(len(rotated[row])):
				rotated[len(rotated) - 1 - col][row] = board[row][col]
	elif rotation == -90:
		for row in range(len(rotated)):
			for col in range(len(rotated[row])):
				rotated[col][len(rotated[row]) - 1 - row] = board[row][col]	
	for row in range(len(rotated)):
		rotated[row] = reduce(lambda a, b: a + b, rotated[row])
	return rotated

if __name__ == '__main__':
	board0 = [  'rnbqkbnr' ,
				'pppppppp' ,
				'________' ,
				'________' ,
				'________' ,
				'________' ,
				'PPPPPPPP' ,
				'RNBQKBNR' ]
	board90 = [ 'RP____pr' ,
				'NP____pn' ,
				'BP____pb' ,
				'QP____pq' ,
				'KP____pk' ,
				'BP____pb' ,
				'NP____pn' ,
				'RP____pr' ]
	board180= [ 'RNBKQBNR' ,
				'PPPPPPPP' ,
				'________' ,
				'________' ,
				'________' ,
				'________' ,
				'pppppppp' ,
				'rnbkqbnr' ]
