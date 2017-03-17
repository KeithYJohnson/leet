from board import Board
from itertools import chain

def test_generate():
    board     = Board()
    width     = 5
    height    = 4

    board.generate(width, height)
    assert len(board.board)    == height
    assert len(board.board[0]) == width

def test_place_mines():
    board = Board()
    board.generate(4,4)
    board.place_mines(4)

    flattened = list(chain.from_iterable(board.board))
    assert(flattened.count("*")) == 4

def test_count_adjacent_mines_per_tile():
    starting_board = [
        ["*",0, 0, 0, 0],
        [ 0, 0, 0, 0,"*"],
        [ 0, 0, 0, 0, 0],
        [ 0, 0,"*",0, 0],
        [ 0, 0, 0, 0, 0]
    ]

    expected = [
        ["*",1, 0, 1, 1],
        [ 1, 1, 0, 1,"*"],
        [ 0, 1, 1, 2, 1],
        [ 0, 1,"*",1, 0],
        [ 0, 1, 1, 1, 0]
    ]

    board = Board()
    board.board = starting_board
    board.count_adjacent_mines_per_tile()
    assert(board.board == expected)

def test_increment_tile():
    starting_board = [
        ["*",0, 0, 0, 0],
        [ 0, 0, 0, 0,"*"],
        [ 0, 0, 0, 0, 0],
        [ 0, 0,"*",0, 0],
        [ 0, 0, 0, 0, 0]
    ]

    expected = [
        ["*",1, 0, 0, 0],
        [ 1, 1, 0, 0,"*"],
        [ 0, 0, 0, 0, 0],
        [ 0, 0,"*",0, 0],
        [ 0, 0, 0, 0, 0]
    ]


    board = Board()
    board.board = starting_board
    board.increment_tile(0,0)
    assert(board.board == expected)

def test_are_coords_in_grid():
    starting_board = [
        ["*",0, 0, 0, 0],
        [ 0, 0, 0, 0,"*"],
        [ 0, 0, 0, 0, 0],
        [ 0, 0,"*",0, 0],
        [ 0, 0, 0, 0, 0]
    ]

    board = Board()
    board.board = starting_board

    assert(board.are_coords_in_grid(-1,0) == False)
    assert(board.are_coords_in_grid(0,-1) == False)
    assert(board.are_coords_in_grid(0, len(starting_board)) == False)
    assert(board.are_coords_in_grid(len(starting_board[0]), 0) == False)
    assert(board.are_coords_in_grid(0,0) == True)
    assert(board.are_coords_in_grid(0,1) == True)
