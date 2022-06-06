import numpy as np
import time
import pandas as pd

class SudokuSolver:
    def __init__(self):
        self.grid = []
        self.grid = np.zeros((9, 9))
        self.test_grid = []
        self.error = 0
        self.default_input()
        self.count = 0
        self.row = 0
        self.col = 0

    def default_input(self):
        self.grid[0][1] = 4
        self.grid[0][4] = 1
        self.grid[0][6] = 9
        self.grid[0][8] = 8

        self.grid[1][0] = 8
        self.grid[1][2] = 5
        self.grid[1][6] = 7

        self.grid[2][7] = 1

        self.grid[3][1] = 2
        self.grid[3][5] = 5
        self.grid[3][8] = 4

        self.grid[4][2] = 1
        self.grid[4][3] = 6

        self.grid[5][1] = 3
        self.grid[5][5] = 8
        self.grid[5][8] = 2

        self.grid[6][7] = 6

        self.grid[7][0] = 3
        self.grid[7][2] = 4
        self.grid[7][6] = 8

        self.grid[8][1] = 8
        self.grid[8][4] = 9
        self.grid[8][6] = 4
        self.grid[8][8] = 3

        self.mirroring()

    def input(self, file: str):
        columns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        csv_file = pd.read_csv(file, sep=';', names=columns, dtype=int)
        for col in range(0, 9):
            for row in range(0, 9):
                self.grid[row][col] = csv_file[col][row]
        self.mirroring()
        print(self.grid)
        print(self.test_grid)

    def mirroring(self):
        self.test_grid = np.zeros((9, 9))
        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] != 0:
                    self.test_grid[row][col] = -1

    def check_line(self, line_num: int):
        for num in range(1, 10):
            found = 0
            for check in range(0, 1):
                for y in range(0, 9):
                    if self.grid[line_num][y] == num:
                        # self.count = self.count + 1
                        if found == 1:
                            self.error = 1
                            # print("Error line - ", line_num)
                        found = 1

    def check_col(self, col_num: int):
        for num in range(1, 10):
            found = 0
            for check in range(0, 1):
                for y in range(0, 9):
                    if self.grid[y][col_num] == num:
                        # self.count = self.count + 1
                        if found == 1:
                            self.error = 1
                            # print("Error col - ", col_num)
                        found = 1

    def check_box(self, x: int, y: int):
        for num in range(1, 10):
            found = 0
            for check in range(0, 1):
                for i in range(0, 3):
                    for j in range(0, 3):
                        if self.grid[x * 3 + i][y * 3 + j] == num:
                            # self.count = self.count + 1
                            if found == 1:
                                self.error = 1
                                # print("Error box - ", x, y)
                            found = 1

    def check_all(self):
        for x in range(0, 9):
            self.check_line(x)
            self.check_col(x)
        for x in range(0, 3):
            for y in range(0, 3):
                self.check_box(x, y)

    def solve(self):
        start = time.time()
        row = 0
        col = 0
        while row < 9:
            if self.test_grid[row][col] != -1:
                if self.grid[row][col] == 9:
                    self.grid[row][col] = 0
                    if col != 0:
                        col = col - 1
                    else:
                        col = 8
                        row = row - 1
                    while self.test_grid[row][col] == -1:
                        if col != 0:
                            col = col - 1
                        else:
                            col = 8
                            row = row - 1
                for number in range(int(self.grid[row][col]) + 1, 10):
                    self.grid[row][col] = number
                    self.check_all()
                    if self.error == 1:
                        self.grid[row][col] = 0
                        self.error = 0
                        if number == 9:
                            if col != 0:
                                col = col - 1
                            else:
                                col = 8
                                row = row - 1
                            while self.test_grid[row][col] == -1:
                                if col != 0:
                                    col = col - 1
                                else:
                                    col = 8
                                    row = row - 1

                    else:
                        col = col + 1
                        if col == 9:
                            col = 0
                            row = row + 1
                        break

            else:
                col = col + 1
                if col == 9:
                    col = 0
                    row = row + 1

        print(self.grid)
        print("Solving time - ", time.time() - start)

    def print(self):
        print(self.grid)

if __name__ == "__main__":
    """
    There is possibility to solve from csv input file
    """
    Sudoku = SudokuSolver()
    Sudoku.print()
    Sudoku.solve()