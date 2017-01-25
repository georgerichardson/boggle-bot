import string
import random

class Board(object):
	def __init__(self):
		pass

	def random_board(self, rows=4, cols=4):
        '''Makes a board of random letters.
        Probably doesn't represent the distribution of letters on a real Boggle board.
        '''
		alphabet = string.ascii_letters.lower()
        board = [[random.choice(alphabet) for col in range(cols)] for row in range(rows)]
		self.rows = rows
		self.cols = cols
		self.tiles = rows * cols
		self.board = board


	def get_paths(self, board):
		pass