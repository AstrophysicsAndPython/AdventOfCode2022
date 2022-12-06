"""Created on Dec 07 01:15:30 2022."""


def list_parser(input_list):
    with open(input_list, 'r') as f:
        cal_list = f.read()

    parsed_list = cal_list.split('\n\n')
    calorie_list = [list(map(int, j)) for j in [i.split('\n') for i in parsed_list]]

    # return max([sum(i) for i in calorie_list])
    total_calories = [sum(i) for i in calorie_list]
    total_calories.sort()

    return sum(total_calories[-3:])
