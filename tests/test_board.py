import pytest

from tetris.board import Board


def test_board_defaults_to_standard_tetris_size_with_empty_row_major_grid():
    board = Board()

    assert board.width == 10
    assert board.height == 20
    assert len(board.grid) == 20
    assert all(len(row) == 10 for row in board.grid)
    assert all(cell == 0 for row in board.grid for cell in row)


def test_can_place_accepts_in_bounds_empty_cells():
    board = Board(width=4, height=4)

    assert board.can_place([(0, 0), (1, 0), (1, 1), (2, 1)], 1, 1)


def test_can_place_rejects_left_right_bottom_and_top_bounds():
    board = Board(width=4, height=4)

    assert not board.can_place([(0, 0)], -1, 0)
    assert not board.can_place([(0, 0)], 4, 0)
    assert not board.can_place([(0, 0)], 0, 4)
    assert not board.can_place([(0, 0)], 0, -1)


def test_can_place_rejects_occupied_cells():
    board = Board(width=4, height=4)
    board.grid[2][1] = 7

    assert not board.can_place([(0, 0), (1, 0)], 1, 2)


def test_place_writes_requested_value_to_all_cells():
    board = Board(width=4, height=4)

    board.place([(0, 0), (1, 0), (1, 1), (2, 1)], 1, 1, value=3)

    assert board.grid[1][1] == 3
    assert board.grid[1][2] == 3
    assert board.grid[2][2] == 3
    assert board.grid[2][3] == 3


def test_place_rejects_invalid_positions_without_partial_writes():
    board = Board(width=4, height=4)

    with pytest.raises(ValueError):
        board.place([(0, 0), (1, 0)], 3, 0, value=5)

    assert all(cell == 0 for row in board.grid for cell in row)


def test_clear_full_lines_compacts_remaining_rows_downward():
    board = Board(width=4, height=5)
    board.grid = [
        [0, 0, 0, 0],
        [9, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 2, 0, 0],
        [3, 3, 3, 3],
    ]

    assert board.clear_full_lines() == 2
    assert board.grid == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [9, 0, 0, 0],
        [0, 2, 0, 0],
    ]


def test_clear_full_lines_returns_zero_when_no_rows_are_full():
    board = Board(width=3, height=2)
    board.grid = [
        [1, 0, 1],
        [0, 1, 0],
    ]

    assert board.clear_full_lines() == 0
    assert board.grid == [
        [1, 0, 1],
        [0, 1, 0],
    ]
