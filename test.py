from nose.tools import raises
from conways import *




def test_board():
    assert Board

def test_cell():
    assert Cell

def test_cell_default_dead():
    cell = Cell()
    assert cell.state == 'dead'

def test_cell_can_be_alive():
    cell = Cell()
    cell.alive()
    assert cell.state == 'alive'

def test_board_size():
    board = Board(rows=5, columns=5)
    assert board.rows == 5
    assert board.columns == 5

def test_get_cell():
    board = Board(rows=5, columns=5)
    assert board.get_cell(1,1).state == 'dead'

def test_count_neighbors():
    board = Board(rows=5, columns=5)
    assert board.count_neighbors(0,0) == 0
    board.get_cell(0,0).alive()
    assert board.count_neighbors(0,1) == 1
