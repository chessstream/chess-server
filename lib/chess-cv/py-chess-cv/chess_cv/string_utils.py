import numpy as np
from game import Location

def board_string_to_location_array(board):
	"""A board string is a python list of 8 strings of 8 characters
	"""
	return np.array([[char_to_location(board[line][c], c, line) 
		for c in range(len(board[line]))] 
		for line in range(len(board))] )

def char_to_location(c, x, y):
	if ord(c) in range(ord('a'), ord('z') + 1):
		color = 'B'
	else:
		color = 'W'
	if c == '_':
		c = None
	return Location(x, y, c, color)

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
	board = [ '________' ,
			  '________' ,
			  '________' ,
			  '________' ,
			  '________' ,
			  '________' ,
			  '________' ,
			  '________' ]
	for row in range(len(locations)):
		for col in range(len(locations[row])):
			if locations[row][col].piece:
				board[row][col] = locations[row][col].piece
	return board

def board_string_to_fen(board, rotation):
	pass

def _rotate_board_string(board, rotation):
	rotated = board[:]
	if rotation == 180:
		rotated = rotated[::-1]
		for row in range(len(rotated)):
			rotated[row] = rotated[row][::-1]
	elif rotation == 90:
		for row in range(len(rotated)):
			for col in range(len(rotated[row])):
				rotated[len(rotated) - 1 - col][row] = board[row][col]
	elif rotation == -90:
		for row in range(len(rotated)):
			for col in range(len(rotated[row])):
				rotated[col][len(rotated[row]) - 1 - row] = board[row][col]		

