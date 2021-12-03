def solve_problem_1(depths):
    increases_in_depth = 0

    for i in range(0, len(depths) - 1):
        if depths[i] < depths[i + 1]:
            increases_in_depth += 1

    print(increases_in_depth)


def solve_problem_2(depths):
    increases_in_depth = 0
    sliding_window_size = 3

    for i in range(0, len(depths) - 1):
        if depths[i:i+sliding_window_size] < depths[i+sliding_window_size:i+sliding_window_size+1]:
            increases_in_depth += 1

    print(increases_in_depth)


if __name__ == '__main__':
    with open("input.txt") as file:
        data = [int(line.strip()) for line in file]

    solve_problem_1(data)
    solve_problem_2(data)
