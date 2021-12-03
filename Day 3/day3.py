from pathlib import Path


def solve_problem_1(binaries):
    nb_of_binaries = len(binaries)
    
    result = [sum(sublist) for sublist in zip(*binaries)]

    gamma_rate_binary = ''.join(map(lambda x: "1" if x > nb_of_binaries/2 else "0", result))
    epsilon_rate_binary = ''.join(map(lambda x: "0" if x > nb_of_binaries/2 else "1", result))

    gamma_rate_decimal = int(gamma_rate_binary, 2)
    epsilon_rate_decimal = int(epsilon_rate_binary, 2)

    print(result, gamma_rate_decimal, epsilon_rate_decimal, gamma_rate_decimal * epsilon_rate_decimal)


def solve_problem_2(binaries):
    length_of_binaries = len(binaries[0])

    # Calculate oxygen
    filtered_binaries = binaries
    for i in range(length_of_binaries):
        if len(filtered_binaries) == 1:
            break

        vertical_slice = [sublist[i] for sublist in filtered_binaries]
        filtered_binaries = list(filter(lambda x: x[i] is int(sum(vertical_slice) >= len(filtered_binaries)/2), filtered_binaries))

    oxygen_rating_binary = ''.join(str(x) for x in filtered_binaries[0])
    oxygen_rating_decimal = int(oxygen_rating_binary, 2)

    # Calculate CO2
    filtered_binaries = binaries
    for i in range(length_of_binaries):
        if len(filtered_binaries) == 1:
            break

        vertical_slice = [sublist[i] for sublist in filtered_binaries]
        filtered_binaries = list(filter(lambda x: x[i] is int(sum(vertical_slice) < len(filtered_binaries)/2), filtered_binaries))

    co2_rating_binary = ''.join(str(x) for x in filtered_binaries[0])
    co2_rating_decimal = int(co2_rating_binary, 2)

    print(oxygen_rating_binary, oxygen_rating_decimal, co2_rating_binary, co2_rating_decimal, oxygen_rating_decimal * co2_rating_decimal)


if __name__ == '__main__':
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as file:
        data = [list(map(int, x)) for x in [list(line.strip()) for line in file]]

    solve_problem_1(data)
    solve_problem_2(data)
