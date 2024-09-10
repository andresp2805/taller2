import sys

def ferry_loading(car_index, remaining_left_space, remaining_right_space, car_lengths, memoization, load_on_left):
    if remaining_left_space <= 0 and remaining_right_space <= 0:
        return 0
    if car_index == len(car_lengths):
        return 0
    if memoization[car_index][remaining_left_space] != -1:
        return memoization[car_index][remaining_left_space]
    load_left = load_right = 0
    if remaining_right_space >= car_lengths[car_index]:
        load_right = ferry_loading(car_index + 1, remaining_left_space, remaining_right_space - car_lengths[car_index], car_lengths, memoization, load_on_left) + 1
    if remaining_left_space >= car_lengths[car_index]:
        load_left = ferry_loading(car_index + 1, remaining_left_space - car_lengths[car_index], remaining_right_space, car_lengths, memoization, load_on_left) + 1
    if load_left > load_right:
        load_on_left[car_index][remaining_left_space] = True
    memoization[car_index][remaining_left_space] = max(load_left, load_right)
    return memoization[car_index][remaining_left_space]

def main():
    input_data = sys.stdin.read().strip().splitlines()
    line_index = 0
    num_cases = int(input_data[line_index].strip())
    line_index += 1
    results = []
    while num_cases > 0:
        while input_data[line_index].strip() == "":
            line_index += 1
        ferry_length = int(input_data[line_index].strip()) * 100
        line_index += 1
        car_lengths = []
        while line_index < len(input_data):
            line = input_data[line_index].strip()
            if line == "0":
                line_index += 1
                break
            elif line == "":
                line_index += 1
                continue
            car_lengths.append(int(line))
            line_index += 1
        memoization = [[-1] * (ferry_length + 1) for _ in range(len(car_lengths))]
        load_on_left = [[False] * (ferry_length + 1) for _ in range(len(car_lengths))]
        max_loaded_cars = ferry_loading(0, ferry_length, ferry_length, car_lengths, memoization, load_on_left)
        results.append(f"{max_loaded_cars}")
        remaining_left_space = ferry_length
        for i in range(max_loaded_cars):
            if load_on_left[i][remaining_left_space]:
                results.append("starboard")
                remaining_left_space -= car_lengths[i]
            else:
                results.append("port")
        num_cases -= 1
        if num_cases > 0:
            results.append("")
    print("\n".join(results))

if __name__ == "__main__":
    main()
