"""Created on Dec 09 00:04:17 2022."""

from _backend__part1 import priority


def rucksack_batch_reorganization(input_file_name):
    rucksacks = file_parser(input_file_name)

    rucksack_batch = get_rucksack_batch(rucksacks)

    common_item = [get_common_item(i) for i in rucksack_batch]

    item_priority = [get_priority(i) for i in common_item]

    return sum(item_priority)


def file_parser(input_file_name):
    with open(input_file_name) as f:
        rucksacks = f.read().split('\n')

    return rucksacks


def get_rucksack_batch(rucksack):
    batch = [rucksack[i:i + 3] for i in range(0, len(rucksack), 3)]

    return batch


def get_priority(item):
    return priority()[item]


def get_common_item(rucksack_batch):
    set1, set2, set3 = [set(i) for i in rucksack_batch]
    return list(set1.intersection(set2.intersection(set3)))[0]
