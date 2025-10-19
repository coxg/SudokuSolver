def is_solved(grid: list[list[int]]) -> bool:
    for row in grid:
        for value in row:
            if not value:
                return False
    return True

def solve(grid: list[list[int]]) -> None:
    width = len(grid)
    if width == 0 or len(grid[0]) != width or width % 3 != 0:
        raise ValueError("Grid must be non-empty and square")

    square_size = width // 3

    has_made_progress = True
    while has_made_progress:
        has_made_progress = False
        for i in range(width):
            for j in range(width):

                # already solved
                if grid[i][j] != 0:
                    continue

                possible_values = [i for i in range(1, width + 1)]

                # remove values from column
                for row in grid:
                    val = row[j]
                    if val in possible_values:
                        possible_values.remove(row[j])

                # remove values from row
                for val in grid[i]:
                    if val in possible_values:
                        possible_values.remove(val)

                # remove values from square
                square_i = i // 3
                square_j = j // 3
                for i_offset in range(square_size):
                    for j_offset in range(square_size):
                        val = grid[square_i * 3 + i_offset][square_j * 3 + j_offset]
                        if val in possible_values:
                            possible_values.remove(val)

                if not possible_values:
                    raise ValueError("Invalid grid")

                if len(possible_values) == 1:
                    grid[i][j] = possible_values[0]
                    has_made_progress = True