from tetris.pieces import (
    TETROMINOES,
    cells,
    rotate_clockwise,
    rotate_counterclockwise,
)


def test_catalog_contains_exactly_the_seven_tetrominoes():
    assert set(TETROMINOES) == {"I", "O", "T", "S", "Z", "J", "L"}


def test_cells_returns_four_unique_integer_offsets_for_every_rotation():
    for kind in TETROMINOES:
        for rotation in range(-4, 8):
            offsets = cells(kind, rotation)

            assert len(offsets) == 4
            assert len(set(offsets)) == 4
            assert all(isinstance(x, int) and isinstance(y, int) for x, y in offsets)
            assert min(x for x, _ in offsets) == 0
            assert min(y for _, y in offsets) == 0


def test_unique_rotation_counts_match_tetromino_symmetry():
    assert _unique_cell_rotations("O") == 1
    assert _unique_cell_rotations("I") == 2
    assert _unique_cell_rotations("S") == 2
    assert _unique_cell_rotations("Z") == 2
    assert _unique_cell_rotations("T") == 4
    assert _unique_cell_rotations("J") == 4
    assert _unique_cell_rotations("L") == 4


def test_rotation_indices_wrap_to_zero_through_three():
    assert rotate_clockwise(0) == 1
    assert rotate_clockwise(3) == 0
    assert rotate_clockwise(7) == 0
    assert rotate_counterclockwise(0) == 3
    assert rotate_counterclockwise(2) == 1
    assert rotate_counterclockwise(-1) == 2


def test_cells_uses_rotation_modulo_four():
    for kind in TETROMINOES:
        assert cells(kind, 0) == cells(kind, 4)
        assert cells(kind, 1) == cells(kind, 5)
        assert cells(kind, -1) == cells(kind, 3)


def test_expected_spawn_orientations_are_normalized():
    assert set(cells("I", 0)) == {(0, 0), (1, 0), (2, 0), (3, 0)}
    assert set(cells("O", 0)) == {(0, 0), (1, 0), (0, 1), (1, 1)}
    assert set(cells("T", 0)) == {(1, 0), (0, 1), (1, 1), (2, 1)}
    assert set(cells("S", 0)) == {(1, 0), (2, 0), (0, 1), (1, 1)}
    assert set(cells("Z", 0)) == {(0, 0), (1, 0), (1, 1), (2, 1)}
    assert set(cells("J", 0)) == {(0, 0), (0, 1), (1, 1), (2, 1)}
    assert set(cells("L", 0)) == {(2, 0), (0, 1), (1, 1), (2, 1)}


def _unique_cell_rotations(kind):
    return len({cells(kind, rotation) for rotation in range(4)})
