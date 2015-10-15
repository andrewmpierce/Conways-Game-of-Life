class Cell():
    def __init__(self, state='dead', neighbors=0):
        self.state = state
        self.neighbors = neighbors

    def alive(self):
        self.state = 'alive'

    def __str__(self):
        return '{}'.format(self.state)


class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.make_grid()


    def make_grid(self):
        grid = [Cell() for x in range(5)]
        grid = [grid for x in range(5)]
        return grid


    def get_cell(self, r, c):
        return self.grid[r][c]


    def count_neighbors(self,r,c):
        options = [-1, 0, 1]
        neighbors = 0
        for x in options:
            if self.grid[r+x][c].state == 'alive' or self.grid[r][c+x].state == 'alive':
                neighbors +=1
        return neighbors


    def assign_neigbors(self):
        options = [0, 1, 2, 3, 4]
        for x in options:
            

board = Board(rows=5, columns=5)
board.make_grid()
