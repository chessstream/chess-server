import numpy as np
import json
import string_utils as su

class Board(object):
	THRESHOLD = 0.01

	def __init__(self, squares):
		"""squares -- a numpy array (8x8) of Square objects """
		self.info = {}

		top = [squares[0][i] for i in range(2, 6)]
		bottom = [squares[7][i] for i in range(2, 6)]
		left = [squares[i][0] for i in range(2, 6)]
		right = [squares[i][7] for i in range(2, 6)]

		# determine camera orientation / board rotation
		# rotation is the angle it must be rotated in order to restore order
		top_avg = sum([sum(square.color_average) for square in top]) / 4
		bottom_avg = sum([sum(square.color_average) for square in bottom]) / 4
		left_avg = sum([sum(square.color_average) for square in left]) / 4
		right_avg = sum([sum(square.color_average) for square in right]) / 4
		lr_diff = abs(left_avg - right_avg)
		tb_diff = abs(top_avg - bottom_avg)
		if lr_diff > tb_diff:
			if left_avg > right_avg:
				# White is on the left
				# Even locations are white
				self.info['rotation'] = 90
				self.info['color'] = ['W', 'B']
				self.info['w_w'] = squares[0][1].color_average
				self.info['b_w'] = squares[0][7].color_average
				self.info['w_b'] = squares[0][0].color_average
				self.info['b_b'] = squares[0][6].color_average
				self.info['x_w'] = squares[0][3].color_average
				self.info['x_b'] = squares[0][4].color_average
				self.info['board'] =  [ 'RP____pr' ,
										'NP____pn' ,
										'BP____pb' ,
										'QP____pq' ,
										'KP____pk' ,
										'BP____pb' ,
										'NP____pn' ,
										'RP____pr' ]
			else:
				# White is on the right
				# Even locations are white
				self.info['rotation'] = -90
				self.info['color'] = ['W', 'B']
				self.info['w_w'] = squares[0][7].color_average
				self.info['b_w'] = squares[0][1].color_average
				self.info['w_b'] = squares[0][6].color_average
				self.info['b_b'] = squares[0][0].color_average
				self.info['x_w'] = squares[0][3].color_average
				self.info['x_b'] = squares[0][4].color_average
				self.info['board'] =  [ 'rp____PR' ,
										'np____PN' ,
										'bp____PB' ,
										'kp____PK' ,
										'qp____PQ' ,
										'bp____PB' ,
										'np____PN' ,
										'rp____PR' ]
		else:
			if top_avg > bottom_avg:
				# White is on the top 
				# Odd locations are white
				self.info['rotation'] = 180
				self.info['color'] = ['B', 'W']
				self.info['w_w'] = squares[0][0].color_average
				self.info['b_w'] = squares[6][0].color_average
				self.info['w_b'] = squares[1][0].color_average
				self.info['b_b'] = squares[7][0].color_average
				self.info['x_w'] = squares[4][0].color_average
				self.info['x_b'] = squares[3][0].color_average
				self.info['board'] =  [ 'RNBKQBNR' ,
										'PPPPPPPP' ,
										'________' ,
										'________' ,
										'________' ,
										'________' ,
										'pppppppp' ,
										'rnbkqbnr' ]
			else:
				# White is on the bottom
				# Odd locations are white
				self.info['rotation'] = 0
				self.info['color'] = ['B', 'W']
				self.info['w_w'] = squares[6][0].color_average
				self.info['b_w'] = squares[0][0].color_average
				self.info['w_b'] = squares[7][0].color_average
				self.info['b_b'] = squares[1][0].color_average
				self.info['x_w'] = squares[4][0].color_average
				self.info['x_b'] = squares[3][0].color_average
				self.info['board'] =  [ 'rnbqkbnr' ,
										'pppppppp' ,
										'________' ,
										'________' ,
										'________' ,
										'________' ,
										'PPPPPPPP' ,
										'RNBQKBNR' ]
		self.info['fen'] = \
			'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
		self.info['to_move'] = 'W'


class Location(object):
	def __init__(self, x, y, piece=None, color=None):
		(self.x, self.y) = (x, y)
		self.piece = piece
		self.color = color

	@property
	def point(self):
		return (self.x, self.y)

	def __repr__(self):
		return str(self.point) + ": " + str(self.piece) \
			+ (", " + str(self.color) if self.piece else "")


def initialize_game(squares):
	board = Board(squares)
	return board.info

def update_game(squares, boardinfo):
	locations = su.board_string_to_location_array(boardinfo['board'])
	disappeared, appeared, taken = \
			compare_square_array_to_location_array(squares, locations)
	update_location_array(locations, squares, disappeared, appeared, taken)
	board = location_array_to_board_string(locations)
	to_move = 'W' if boardinfo['to_move'] == 'B' else 'B'
	fen = board_string_to_fen(board, rotation, to_move)
	boardinfo['board'] = board
	boardinfo['to_move'] = to_move
	boardinfo['fen'] = fen
	return boardinfo

def main():
	pass

if __name__ == '__main__':
	main()