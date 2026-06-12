"""Tetromino catalog and rotation helpers."""


_SPAWN_SHAPES = {
    "I": ((0, 0), (1, 0), (2, 0), (3, 0)),
    "O": ((0, 0), (1, 0), (0, 1), (1, 1)),
    "T": ((1, 0), (0, 1), (1, 1), (2, 1)),
    "S": ((1, 0), (2, 0), (0, 1), (1, 1)),
    "Z": ((0, 0), (1, 0), (1, 1), (2, 1)),
    "J": ((0, 0), (0, 1), (1, 1), (2, 1)),
    "L": ((2, 0), (0, 1), (1, 1), (2, 1)),
}


def rotate_clockwise(rotation):
    """Return the next clockwise rotation index in the 0..3 range."""
    return (rotation + 1) % 4


def rotate_counterclockwise(rotation):
    """Return the next counterclockwise rotation index in the 0..3 range."""
    return (rotation - 1) % 4


def cells(kind, rotation):
    """Return four normalized (x, y) offsets for kind at rotation."""
    rotations = TETROMINOES[kind]
    rotation_index = (rotation % 4) % len(rotations)
    return rotations[rotation_index]


def _build_catalog():
    return {kind: _unique_rotations(shape) for kind, shape in _SPAWN_SHAPES.items()}


def _unique_rotations(shape):
    rotations = []
    current = tuple(shape)

    for _ in range(4):
        normalized = _normalize(current)
        if normalized not in rotations:
            rotations.append(normalized)
        current = _rotate_shape_clockwise(current)

    return tuple(rotations)


def _rotate_shape_clockwise(shape):
    return tuple((y, -x) for x, y in shape)


def _normalize(shape):
    min_x = min(x for x, _ in shape)
    min_y = min(y for _, y in shape)
    return tuple(sorted((x - min_x, y - min_y) for x, y in shape))


TETROMINOES = _build_catalog()
