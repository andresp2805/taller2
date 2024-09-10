import sys

def calculate_min_cut_cost(start, end, cut_positions, dp_table):
    if end - start == 1:
        return 0
    if dp_table[start][end] != -1:
        return dp_table[start][end]
    min_cost = float('inf')
    for cut_index in range(start + 1, end):
        cost = (cut_positions[end] - cut_positions[start] + calculate_min_cut_cost(start, cut_index, cut_positions, dp_table) + calculate_min_cut_cost(cut_index, end, cut_positions, dp_table))
        min_cost = min(min_cost, cost)
    dp_table[start][end] = min_cost
    return min_cost

def main()->None:
    input_data = sys.stdin.read().strip().splitlines()
    line_index = 0
    results = []
    while line_index < len(input_data):
        stick_length = int(input_data[line_index].strip())
        line_index += 1
        if stick_length == 0:
            break
        num_cuts = int(input_data[line_index].strip())
        line_index += 1
        cut_positions = list(map(int, input_data[line_index].split()))
        line_index += 1
        cut_positions = [0] + cut_positions + [stick_length]
        dp_table = [[-1 for _ in range(len(cut_positions))] for _ in range(len(cut_positions))]
        min_cost = calculate_min_cut_cost(0, len(cut_positions) - 1, cut_positions, dp_table)
        results.append(f"The minimum cutting is {min_cost}.")
    print("\n".join(results))

if __name__ == "__main__":
    main()