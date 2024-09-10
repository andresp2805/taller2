import sys
import bisect

def calculate_longest_train(car_weights):
    num_cars = len(car_weights)
    increasing_seq = []
    decreasing_seq = []
    max_train_length = 0
    for i in range(num_cars - 1, -1, -1):
        car_weight = car_weights[i]
        lis_position = bisect.bisect_left(increasing_seq, car_weight)
        lds_position = bisect.bisect_right(decreasing_seq, car_weight)

        if lis_position == len(increasing_seq):
            increasing_seq.append(car_weight)
            lis_length = len(increasing_seq)
        else:
            increasing_seq[lis_position] = car_weight
            lis_length = lis_position + 1
        
        if lds_position == 0:
            decreasing_seq.insert(0, car_weight)
            lds_length = len(decreasing_seq)
        else:
            decreasing_seq[lds_position - 1] = car_weight
            lds_length = len(decreasing_seq) - (lds_position - 1)
        max_train_length = max(max_train_length, lis_length + lds_length - 1)
    return max_train_length

def main():
    input_data = sys.stdin.read().strip().splitlines()
    line_index = 0
    test_cases = int(input_data[line_index].strip())
    line_index += 1
    results = []
    while test_cases > 0:
        num_cars = int(input_data[line_index].strip())
        line_index += 1
        car_weights = []
        for _ in range(num_cars):
            car_weights.append(int(input_data[line_index].strip()))
            line_index += 1
        result = calculate_longest_train(car_weights)
        results.append(result)
        test_cases -= 1
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
