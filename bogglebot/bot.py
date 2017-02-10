import string
import random
from nltk import 

class Board(object):
    def __init__(self):
        pass

    def random_board(self, rows=4, cols=4):
        '''Makes a board of random letters.

        DOES NOT represent the distribution of letters on a real Boggle board.
        '''
        alphabet = string.ascii_letters.lower()
        board = [[random.choice(alphabet) for col in range(cols)] for row in range(rows)]
        self.rows = rows
        self.cols = cols
        self.tiles = rows * cols
        self.board = board

        return self.board

    def random_board_big(self):
        '''Makes a 5x5 board of letters randomly selected from the shuffled die in Boggle.
        '''
        die = ['aaafrs', 'aaeeee', 'aafirs', 'adennn', 'aeeeem',
               'aeegmu', 'aegmnn', 'afirsy', 'bjkqxz', 'ccnstw',
               'ceiilt', 'ceilpt', 'ceipst', 'dhhnot', 'dhhlor',
               'dhlnor', 'ddlnor', 'eiiitt', 'emottt', 'ensssu',
               'fiprsy', 'gorrvw', 'hiprry', 'nootuw', 'ooottu']
        random.shuffle(die)
        board = [[random.choice(die.pop()) for col in range(5)] for row in range(5)]
        return self.board


    def random_board_small(self):
        '''Makes a 4x4 board of letters randomly selected from the shuffled die in Boggle.
        '''
        die = ['aaeegn', 'elrtty', 'aoottw', 'abbjoo',
               'ehrtvw', 'cimotu', 'distty', 'eiosst', 
               'delrvy', 'achops', 'himnqu', 'eeinsu',
               'eeghnw', 'affkps', 'hlnnrz', 'deilrx']
        random.shuffle(die)
        board = [[random.choice(die.pop()) for col in range(4)] for row in range(4)]
        return self.board

    def get_webboggle_board(self, url):
        pass


class BoggleBot(object):
    def __init__(self, board):
        self.board = board

    def find_paths(self, board, min_length=3, output=False):
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
        return paths

    def letter_combos(self, board):
        ''' Returns a list of all the possible letter combinations on the board.
        '''
        self.letter_combos = [''.join([self.board[row][col] for row, col in path]) for path in self.paths]
        return letter_combos

    def english_words(self, letter_combos):
        '''Retrieves english words from list of letter combinations.
        '''
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        self.english_words = [word for word in letter_combos if word in english_vocab]
        return self.english_words

    def word_score(self):
        '''Calculate boggle score of English words found on board.
        '''
        self.word_score = {word: len(word)-2 for word in self.english_words}
        return self.word_score

    def total_score(self):
        '''Find total Boggle score of English words on board.
        '''
        self.total_score = sum(self.word_score.values())
        return self.total_score

class Student(object):
    '''Uses a BoggleBot as a teacher to learn the English vocabulary.
    '''

    def __init__(self):
        pass

    def lesson(self, show=False):
        '''
        Learns from a board and a bot (teacher)
        '''
        board = Board()
        board = random_board_small()
        teacher = BoggleBot(board)
        letter_combos = techer.letter_combos(board)
        total_score = teacher.total_score()

