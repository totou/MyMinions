# Initial commit
# Getting ready for the minions

import copy
import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Grid(list):
    """
    Class representing the Grid
    x = Column
    y = Row
    0,0 bottom left ; 0,12 top left ; 6,0 bottom right ; 6,12 top right
    """
    def __init__(self, *args):
        list.__init__(self, *args)
        for i in range(0, 6):
            self.append([])
            for _ in range(0, 12):
                self[i].append(None)

    def fill_row(self, row_num, row_numbers):
        # print("Filling row {0}".format(row_num), file=sys.stderr)
        for i, v in enumerate(row_numbers):
            if v != '.':
                v = int(v)
                if 0 <= v < global_max_color:
                    self[i][row_num] = v
                else:
                    self[i][row_num] = None
            else:
                self[i][row_num] = None

    def next_row_num_of_column(self, column):
        return self[column].index(None)  # Return index of the first None

    def display_row(self, row):
        res = ""
        for c in range(len(self)):
            if self[c][row] is not None:
                res += "{} ".format(self[c][row])
            else:
                res += "N "
        return res

    def __str__(self):
        res = ""
        for row in range(len(self[0])-1, -1, -1):
            res += "\nRow {0:02d}: {1}".format(row, self.display_row(row))
        return res


class GameStatus(object):

    def __init__(self, next_colors, my_grid, enemy_grid, turn_num=0, my_points=0, enemy_points=0, blocks=0, my_nuisance=0, enemy_nuisance=0):
        self.turn_num = turn_num
        self.next_colors = next_colors[self.turn_num:]
        self.my_grid = my_grid
        self.enemy_grid = enemy_grid
        self.my_points = my_points
        self.enemy_points = enemy_points
        self.blocks = blocks
        self.my_nuisance = my_nuisance
        self.enemy_nuisance = enemy_nuisance

    def __str__(self):
        return "turn {}\nnext_colors {}\nmygrid {}\nenemy_grid {}\nmy_points {}\nenemy_points {}\n" \
               "blocks {}\nmy_nuisance {}\nenemy_nuisance {}".format(
                self.turn_num, self.next_colors, self.my_grid, self.enemy_grid, self.my_points, self.enemy_points,
                self.blocks, self.my_nuisance, self.enemy_nuisance)


class GameEngine(object):

    def __init__(self, game_status):
        self.game_status = game_status

    def calculate_next_turn(self):
        # TODO
        new_game_status = GameStatus(self.game_status.next_colors, self.game_status.turn_num + 1, ...)
        return new_game_status

    def calculate_next_grid(self, curr_grid, block, drop_column):
        next_grid = copy.deepcopy(curr_grid)
        self.insert_block_in_grid(next_grid, block, drop_column)
        return next_grid

    @staticmethod
    def insert_block_in_grid(grid, b, column_a, column_b=None):
        row_a = grid.next_row_num_of_column(column_a)
        grid[row_a] = b[0]
        if column_b is None:
            grid[row_a+1] = b[1]
        else:
            grid[grid.next_row_num_of_column(column_b)] = b[1]


class ComputeOutput(object):

    def __init__(self, game_status=None):
        self.game_status = game_status

    def new_status(self, game_status):
        # print("New game status {0}".format(game_status), file=sys.stderr)
        self.game_status = copy.deepcopy(game_status)

    def execute(self):
        """This is the main function that will compute the output"""
        # print("Get game status: {0}".format(self.game_status), file=sys.stderr)
        return int(self.game_status.next_colors[0][0])-1

# Globals
global_max_color = 6
global_compute_output = ComputeOutput()

# game loop
while True:

    next_colors = []
    my_grid = Grid()
    enemy_grid = Grid()

    for i in range(8):
        # color_a: color of the first block
        # color_b: color of the attached block
        color_a, color_b = [int(j) for j in input().split()]
        next_colors.append((color_a, color_b))
    # print("Next colors {0}".format(next_colors), file=sys.stderr)
    for i in range(11, -1, -1):  # Rows are given top first (height 12)
        row = input()
        my_grid.fill_row(i, row)
    # print("My Grid {0}".format(my_grid), file=sys.stderr)
    for i in range(11, -1, -1):
        row = input()  # One line of the map ('.' = empty, '0' = skull block, '1' to '5' = colored block)
        enemy_grid.fill_row(i, row)
    # print("Enemy Grid {0}".format(enemy_grid), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    global_compute_output.new_status(GameStatus(next_colors, my_grid, enemy_grid))

    # "x": the column in which to drop your blocks
    print("{0}".format(global_compute_output.execute()))
