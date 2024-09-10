import sys

def diving_for_glod(time_limit: int, treasure_index: int, values: list[int], depths: list[int], w: int) -> tuple:
    dp = [[0] * (time_limit + 1) for _ in range(treasure_index + 1)]    
    for i in range(1, treasure_index + 1):
        time_needed = 3 * w * depths[i - 1]
        for j in range(time_limit + 1):
            if time_needed > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - time_needed])
    max_gold = dp[treasure_index][time_limit]
    return dp, max_gold

def find_selected_treasures(time_limit: int, values: list[int], depths: list[int], w: int, dp: list[list[int]]) -> list[int]:
    selected = []
    treasure_index = len(values)
    for i in range(treasure_index, 0, -1):
        time_needed = 3 * w * depths[i - 1]
        if dp[i][time_limit] != dp[i - 1][time_limit]:
            selected.append(i - 1)
            time_limit -= time_needed
    selected.reverse() 
    return selected

def main()->None:
    input_data = sys.stdin.read().strip().splitlines()
    i = 0
    first_case = True 
    
    with open("990.out", "w") as output_file:
        while i < len(input_data):
            if input_data[i] == "":
                i += 1
                continue
            
            time_limit, w = map(int, input_data[i].split())
            i += 1
            
            treasure_index = int(input_data[i])
            i += 1
            
            depths = []
            values = []
            
            for _ in range(treasure_index):
                depth, value = map(int, input_data[i].split())
                depths.append(depth)
                values.append(value)
                i += 1
            
            dp, max_gold = diving_for_glod(time_limit, treasure_index, values, depths, w)
            
            selected_treasures = find_selected_treasures(time_limit, values, depths, w, dp)
            
            if not first_case:
                print()
            first_case = False
            print(max_gold)
            print(len(selected_treasures))
            for idx in selected_treasures:
                print(depths[idx], values[idx])

if __name__ == "__main__":
    main()
