"""Board state and row-clearing logic for terminal Tetris."""


class Board:
    """A rectangular Tetris playfield stored as row-major grid cells."""

    def __init__(self, width=10, height=20):
        if width <= 0:
            raise ValueError("width must be positive")
        if height <= 0:
            raise ValueError("height must be positive")

        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def can_place(self, cells, x, y):
        """Return True when all cell offsets fit inside empty board cells."""
        for cell_x, cell_y in cells:
            board_x = x + cell_x
            board_y = y + cell_y

            if board_x < 0 or board_x >= self.width:
                return False
            if board_y < 0 or board_y >= self.height:
                return False
            if self.grid[board_y][board_x]:
                return False

        return True

    def place(self, cells, x, y, value=1):
        """Lock cells into the board using value after validating placement."""
        cells = tuple(cells)
        if not self.can_place(cells, x, y):
            raise ValueError("cells cannot be placed at the requested position")

        for cell_x, cell_y in cells:
            self.grid[y + cell_y][x + cell_x] = value

    def clear_full_lines(self):
        """Clear full rows, compact remaining rows downward, and return count."""
        remaining_rows = [row for row in self.grid if not _is_full(row)]
        cleared = self.height - len(remaining_rows)

        empty_rows = [[0 for _ in range(self.width)] for _ in range(cleared)]
        self.grid = empty_rows + remaining_rows

        return cleared


def _is_full(row):
    return all(row)
