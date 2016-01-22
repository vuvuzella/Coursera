"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random
# try:
from merge import merge as merge
# except Exception:
#    import user41_QHoxAHH95t_0 as merge

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.i_height = grid_height
        self.i_width = grid_width
        self.arr_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
        self.zero_index = {UP: [(0, col) for col in range(grid_width)],
                           DOWN: [(grid_height-1, col) for col in range(grid_width)],
                           LEFT: [(row, 0) for row in range(grid_height)],
                           RIGHT: [(row, grid_width-1) for row in range(grid_height)]}
        self.reset()
        self.FINISHED = 0
        self.moved = 0
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_grid = "[\n"
        for row in range(self.get_grid_height()):
            str_grid += " ["
            for col in range(self.get_grid_width()):
                str_grid += str((self.arr_grid[row][col]))
                if col < self.get_grid_width() - 1:
                    str_grid += " "
            str_grid += "],\n"
        str_grid += "]"
        return str_grid

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        for i_index_y in range(self.get_grid_width()):
            for i_index_x in range(self.get_grid_height()):
                self.arr_grid[i_index_x][i_index_y] = 0
        self.new_tile()
        self.new_tile()
        return self.arr_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.i_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.i_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if self.FINISHED == 1:
            return
        arr_offset = OFFSETS[direction]
        arr_start_index = self.zero_index[direction]
        arr_merge = []

        # get the UP grid merging
        for row, col in arr_start_index:
            i_count = 0
            if direction == UP or direction == DOWN:
                while i_count < self.get_grid_height():
                    arr_merge.append(self.get_tile(row + (arr_offset[0] * i_count),
                                                   col + (arr_offset[1] * i_count)))
                    i_count += 1
            else:
                while i_count < self.get_grid_width():
                    arr_merge.append(self.get_tile(row + (arr_offset[0] * i_count),
                                                   col + (arr_offset[1] * i_count)))
                    i_count += 1
            """
            for row_count in range(self.get_grid_height()):
                for col_count in range(self.get_grid_width()):
                    arr_merge.append(self.get_tile(row + (arr_offset[0] * row_count),
                                                   col + (arr_offset[1] * col_count)))
            """
            # print "row:%d col:%d" % (row, col)
            # print arr_merge
            arr_merged = merge(arr_merge)
            i_count = 0
            if direction == UP or direction == DOWN:
                while i_count < self.get_grid_height():
                    print "pre-merge:%d, post-merge:%d" % (arr_merge[i_count], arr_merged[i_count])
                    if arr_merge[i_count] != arr_merged[i_count]:
                        self.moved = 1
                    self.set_tile(row + (arr_offset[0] * i_count),
                                  col + (arr_offset[1] * i_count), arr_merged[i_count])
                    i_count += 1
            else:
                while i_count < self.get_grid_width():
                    print "pre-merge:%d, post-merge:%d" % (arr_merge[i_count], arr_merged[i_count])
                    if arr_merge[i_count] != arr_merged[i_count]:
                        self.moved = 1
                    self.set_tile(row + (arr_offset[0] * i_count),
                                  col + (arr_offset[1] * i_count), arr_merged[i_count])
                    i_count += 1
            del arr_merge[:]
            del arr_merged[:]
        if self.moved:
            self.moved = 0
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        arr_random_open_tile = self.get_open_tile()
        if not arr_random_open_tile:
            self.FINISHED = 1
            return
        arr_random_tile = arr_random_open_tile[random.randrange(
            len(arr_random_open_tile))]
        i_row = arr_random_tile[0]
        i_col = arr_random_tile[1]
        input_num = 0
        xrand = random.randint(1, 100)
        if xrand <= 10:
            input_num = 4
        else:
            input_num = 2

        """
        # not supported in codeskulptor
        num = [[2, 0.90], [4, 0.10]]
        uniform = random.uniform(0, 1)
        upto = 0
        input_num = 0
        for choice, weight in num:
            # print "c is %d, w is %f" % (choice, weight)
            if upto + weight >= uniform:
                input_num = choice
                break
            upto += weight
        """
        self.arr_grid[i_row][i_col] = input_num


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.arr_grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.arr_grid[row][col]

    def get_open_tile(self):
        """
        Returns an array of y,x values that are empty
        """
        arr_open_tiles = []
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self.arr_grid[row][col] == 0:
                    arr_open_tiles.append([row, col])
        return arr_open_tiles


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
