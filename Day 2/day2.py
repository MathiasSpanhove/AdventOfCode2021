from pathlib import Path


def solve_problem_1(commands):
    horizontal_pos = 0
    vertical_pos = 0

    for command in commands:
        action, value = command.split(" ")

        if action == "forward":
            horizontal_pos += int(value)
        elif action == "down":
            vertical_pos += int(value)
        elif action == "up":
            vertical_pos -= int(value)

    print(horizontal_pos, vertical_pos, horizontal_pos * vertical_pos)


def solve_problem_2(commands):
    horizontal_pos = 0
    vertical_pos = 0
    aim = 0

    for command in commands:
        action, value = command.split(" ")

        if action == "forward":
            horizontal_pos += int(value)
            vertical_pos += int(value) * aim
        elif action == "down":
            aim += int(value)
        elif action == "up":
            aim -= int(value)

    print(horizontal_pos, vertical_pos, horizontal_pos * vertical_pos)


if __name__ == '__main__':
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as file:
        data = [line.strip() for line in file]

    solve_problem_1(data)
    solve_problem_2(data)
