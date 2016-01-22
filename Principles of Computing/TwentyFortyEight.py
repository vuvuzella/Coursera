"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random
from merge import merge as merge

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
        self.arr_grid = [[0 for y in range(grid_width)] for x in range(grid_height)]
        self.zero_index = {UP: [(0, x_index) for x_index in range(grid_width)],
                           DOWN: [(grid_height-1, x_index) for x_index in range(grid_height)],
                           LEFT: [(y_index, 0) for y_index in range(grid_width)],
                           RIGHT: [(y_index, grid_width-1) for y_index in range(grid_height)]}
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_grid = "[\n"
        for y_index in range(self.get_grid_width()):
            str_grid += " ["
            for x_index in range(self.get_grid_height()):
                str_grid += str((self.arr_grid[y_index][x_index]))
                if x_index < self.get_grid_height() - 1:
                    str_grid += " "
            str_grid += "],\n"
        str_grid += "]"
        return str_grid

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        for i_index_x in range(self.get_grid_width()):
            for i_index_y in range(self.get_grid_height()):
                self.arr_grid[i_index_x][i_index_y] = 0
        # self.new_tile()
        # self.new_tile()
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
        arr_offset = OFFSETS[direction]
        arr_start_index = self.zero_index[direction]
        arr_merge = []

        # get the UP grid merging
        for y_index, x_index in arr_start_index:
            i_count = 0
            # print "(%d %d)" % (y_index, x_index)
            # arr_merge.append(self.get_tile(y_index, x_index))
            if direction == UP or direction == DOWN:
                while i_count < self.get_grid_height():
                    arr_merge.append(self.get_tile(y_index + (arr_offset[0] * i_count),
                                                   x_index + (arr_offset[1] * i_count)))
                    i_count += 1
            else:
                while i_count < self.get_grid_width():
                    arr_merge.append(self.get_tile(y_index + (arr_offset[0] * i_count),
                                                   x_index + (arr_offset[1] * i_count)))
                    i_count += 1
            arr_merged = merge(arr_merge)
            # print arr_merged
            i_count = 0
            if direction == UP or direction == DOWN:
                # self.set_tile(y_index, x_index, arr_merged[0])
                while i_count < self.get_grid_height():
                    # print self
                    # print self.get_tile(y_index + arr_offset[0], x_index + arr_offset[1])
                    self.set_tile(y_index + (arr_offset[0] * i_count),
                                  x_index + (arr_offset[1] * i_count), arr_merged[i_count])
                    i_count += 1
            else:
                while i_count < self.get_grid_width():
                    self.set_tile(y_index + (arr_offset[0] * i_count),
                                  x_index + (arr_offset[1] * i_count), arr_merged[i_count])
                    i_count += 1
            del arr_merge[:]
            del arr_merged[:]

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        arr_random_open_tile = self.get_open_tile()
        arr_random_tile = arr_random_open_tile[random.randrange(
            len(arr_random_open_tile))]
        i_row = arr_random_tile[0]
        i_col = arr_random_tile[1]
        num = [[2, 0.90], [4, 0.10]]
        total = sum(weight for choice, weight in num)
        uniform = random.uniform(0, 1)
        upto = 0
        input_num = 0
        for choice, weight in num:
            # print "c is %d, w is %f" % (choice, weight)
            if upto + weight >= uniform:
                input_num = choice
                break
            upto += weight
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
        for y_index in range(self.get_grid_height()):
            for x_index in range(self.get_grid_width()):
                if self.arr_grid[y_index][x_index] == 0:
                    arr_open_tiles.append([y_index, x_index])
        return arr_open_tiles


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
