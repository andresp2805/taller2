import sys

def max_sum_on_torus(grid_size, grid):
    expanded_size = grid_size + grid_size
    expanded_grid = [[0] * (expanded_size + 1) for _ in range(expanded_size + 1)]

    for row in range(1, grid_size + 1):
        for col in range(1, grid_size + 1):
            expanded_grid[row][col] = grid[row - 1][col - 1]
            expanded_grid[row + grid_size][col] = grid[row - 1][col - 1]
            expanded_grid[row][col + grid_size] = grid[row - 1][col - 1]
            expanded_grid[row + grid_size][col + grid_size] = grid[row - 1][col - 1]

    for row in range(1, expanded_size + 1):
        for col in range(1, expanded_size + 1):
            expanded_grid[row][col] += expanded_grid[row - 1][col] + expanded_grid[row][col - 1] - expanded_grid[row - 1][col - 1]

    max_subrectangle_sum = -float('inf')

    for top_row in range(1, grid_size + 1):
        for left_col in range(1, grid_size + 1):
            for bottom_row in range(top_row, top_row + grid_size):
                for right_col in range(left_col, left_col + grid_size):
                    current_sum = (expanded_grid[bottom_row][right_col] - expanded_grid[top_row - 1][right_col]
                                   - expanded_grid[bottom_row][left_col - 1] + expanded_grid[top_row - 1][left_col - 1])
                    max_subrectangle_sum = max(max_subrectangle_sum, current_sum)

    return max_subrectangle_sum

def main()->None:
    input_data = sys.stdin.read().strip().splitlines()
    line_index = 0
    test_cases = int(input_data[line_index])
    line_index += 1
    results = []

    while line_index < len(input_data):
        if input_data[line_index] == "":
            line_index += 1
            continue

        grid_size = int(input_data[line_index])
        line_index += 1
        grid = []

        for _ in range(grid_size):
            grid.append(list(map(int, input_data[line_index].split())))
            line_index += 1

        result = max_sum_on_torus(grid_size, grid)
        results.append(result)

    print("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()