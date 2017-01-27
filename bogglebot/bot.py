import string
import random
from nltk import 

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

    def get_webboggle_board(self, url):
        pass

	def get_paths(self, board, min_length=3, output=False):
		'''Finds and returns all of the possible word paths on the board.

        Returns:
        paths - all of the possible pathways on the board above the minimum
        length threshold
        '''
        # create queue of starting coordinates, starting with points of letters
        queue = [[(row, col) for col in range(self.cols)] for row in range(self.rows)]
        # add all starting points to final output
        paths = [path for path in queue if len(path) >= min_length]
        # possible steps that can be taken from any tile
        steps = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

        # while there are still items in the queue
        while queue:
        # pop last path tuple list from end of queue
        start_path = queue.pop()
        # use last coordinate of the path as new search point
        start_row, start_col = start_path[-1]
        # search for possible steps around the point
        for drow, dcol in steps:
            row2 = start_row + drow
            col2 = start_col + dcol
            new_path = start_path.copy()
            if 0 <= row2 < row_length and 0 <= col2 < col_length:
                # check if point already exists in path
                if (row2, col2) not in start_path:
                    # add path to final paths list and to queue
                    new_path.append((row2, col2))
                    queue.append(new_path)
                    if len(path) >= min_length:
                        paths.append(new_path)

        self.paths = paths

    def letter_combos(self):
        letter_combos = [[self.board[row][col] for row, col in path] for path in self.paths]
        return letter_combos



class BoggleBot(object):
    def __init__(self):
        pass

    def english_words(self, words):
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        
        



    def score(self):
        pass