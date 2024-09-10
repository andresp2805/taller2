import sys

def calculate_max_height(block_idx, dp, dependencies, blocks):
    if dp[block_idx] != -1:
        return dp[block_idx]
    max_height = 0
    for dependent_block in dependencies[block_idx]:
        max_height = max(max_height, calculate_max_height(dependent_block, dp, dependencies, blocks))
    dp[block_idx] = max_height + blocks[block_idx][2]
    return dp[block_idx]

def can_place_on_top(upper_block, lower_block):
    upper_x, upper_y, _ = upper_block
    lower_x, lower_y, _ = lower_block
    return (upper_x < lower_x and upper_y < lower_y) or (upper_x < lower_y and upper_y < lower_x)

def main()->None:
    input_data = sys.stdin.read().strip().splitlines()
    case_num = 1
    results = []
    line_index = 0
    while line_index < len(input_data):
        num_blocks = int(input_data[line_index].strip())
        line_index += 1
        if num_blocks == 0:
            break
        blocks = []
        for _ in range(num_blocks):
            a, b, c = map(int, input_data[line_index].split())
            line_index += 1
            blocks.append([a, b, c])
            blocks.append([b, c, a])
            blocks.append([c, a, b])
        total_blocks = len(blocks)
        dependencies = [[] for _ in range(total_blocks)]
        for i in range(total_blocks):
            for j in range(total_blocks):
                if can_place_on_top(blocks[i], blocks[j]):
                    dependencies[j].append(i)
        dp = [-1] * total_blocks
        max_tower_height = 0
        for i in range(total_blocks):
            max_tower_height = max(max_tower_height, calculate_max_height(i, dp, dependencies, blocks))
        results.append(f"Case {case_num}: maximum height = {max_tower_height}")
        case_num += 1
    print("\n".join(results))
    
if __name__ == "__main__":
    main()