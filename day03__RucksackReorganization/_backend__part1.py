"""Created on Dec 08 23:41:39 2022."""


def rucksack_reorganization(input_file_name):
    rucksacks = file_parser(input_file_name)

    rucksack_length = [len(rucksack) for rucksack in rucksacks]

    rucksack_items = [divide_rucksack_in_two(i, j) for i, j in zip(rucksacks, rucksack_length)]

    common_item = [get_common_item(item) for item in rucksack_items]

    get_total = [get_value(i) for i in common_item]

    return sum(get_total)


def file_parser(input_file_name):
    with open(input_file_name) as f:
        rucksacks = f.read().split('\n')

    return rucksacks


def divide_rucksack_in_two(rucksack, rucksack_length):
    half_length = rucksack_length // 2
    return [rucksack[0:half_length], rucksack[half_length:]]


def get_common_item(rucksack_pair):
    set1, set2 = [set(i) for i in rucksack_pair]
    return list(set1.intersection(set2))[0]


def get_value(item):
    return priority()[item]


def priority():
    lower_case_alphabets = [chr(i, ) for i in list(range(ord('a'), ord('z') + 1))]
    upper_case_alphabets = [chr(i, ) for i in list(range(ord('A'), ord('Z') + 1))]

    lower_case_alphabets__values = list(range(1, 27))
    upper_case_alphabets__values = list(range(27, 53))

    lower_case_alphabets.extend(upper_case_alphabets)
    lower_case_alphabets__values.extend(upper_case_alphabets__values)

    return dict([(key, value) for key, value in zip(lower_case_alphabets, lower_case_alphabets__values)])
