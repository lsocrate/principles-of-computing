"""
Clone of 2048 game.
"""

import user34_BBrd1qseMF_2 as test_merge
import user34_YK0tFwIrdd_6 as test_2048

import poc_2048_gui

import random


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

def zeroes_to_the_end(a, b):
    if a is 0:
        return 1
    elif b is 0:
        return -1
    else:
        return 0

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    moved = sorted(line, zeroes_to_the_end)

    for index in range(len(moved)):
        if index <= len(moved) - 2 and moved[index] is moved[index + 1]:
            moved[index] += moved[index + 1]
            del moved[index + 1]
            moved.append(0)

    return moved

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        self.setup_borders()

    def setup_borders(self):
        height = self.get_grid_height()
        width = self.get_grid_width()

        self._top = tuple( (0, index) for index in range(width) )
        self._right = tuple( (index, width - 1) for index in range(height) )
        self._bottom = tuple( (height - 1, index) for index in range(width) )
        self._left = tuple( (index, 0) for index in range(height) )

    def _get_empty_tiles(self):
        """
        Retrieve list of empty tiles as tuples (row x col)
        """
        empty_tiles = []
        for (row_n, row) in enumerate(self._grid):
            for (col_n, tile) in enumerate(row):
                if tile is 0:
                    empty_tiles.append((row_n, col_n))

        return empty_tiles

    def _get_baseline_for_direction(self, direction):
        if direction is UP:
            return self._top
        elif direction is RIGHT:
            return self._right
        elif direction is DOWN:
            return self._bottom
        elif direction is LEFT:
            return self._left

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self._grid = cells = [ [0 for col in range(self._width)] for row in range(self._height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return '\n'.join(map(str, self._grid))

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        for (row, col) in self._get_baseline_for_direction(direction):
            print (direction, row, col)
            (row_offset, col_offset) = OFFSETS[direction]

            (current_row, current_col) = (row, col)
            line = [self.get_tile(current_row, current_col)]
            while line[-1] is not None:
                current_row += row_offset
                current_col += col_offset
                line.append(self.get_tile(current_row, current_col))
            line.pop()

            merged = merge(line)
            (merging_row, merging_col) = (row, col)
            for value in merged:
                self.set_tile(merging_row, merging_col, value)
                merging_row += row_offset
                merging_col += col_offset

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        (tile_row, tile_col) = random.choice(self._get_empty_tiles())
        tile_value = 2 if random.randrange(1, 101) <= 90 else 4
        self._grid[tile_row][tile_col] = tile_value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        try:
            self._grid[row][col] = value
        except IndexError:
            pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        try:
            return self._grid[row][col]
        except IndexError:
            return None


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

test_merge.run_test(merge)
test_2048.run_test(TwentyFortyEight)
