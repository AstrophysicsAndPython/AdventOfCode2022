"""Created on Dec 09 00:25:02 2022."""


def camp_cleanup_processing(input_file_name):
    cleanup_duties = file_parser(input_file_name)

    groups = [split_groups(i) for i in cleanup_duties]

    range_ = [generate_range(i) for i in groups]

    _ = [get_list_of_cleanup_duties(i) for i in range_]

    return sum([check_duplicates(i) for i in _])


def check_duplicates(list_of_duties):
    duty1 = set(list_of_duties[0])
    duty2 = set(list_of_duties[1])

    # cond1 = set(duty1).intersection(set(duty2)) == set(duty2)
    # cond2 = set(duty2).intersection(set(duty1)) == set(duty1)

    cond1 = set(duty1).intersection(set(duty2)) != set()
    cond2 = set(duty2).intersection(set(duty1)) != set()

    return 1 if any([cond1, cond2]) else 0


def get_list_of_cleanup_duties(duty_list):
    l1 = list(range(*duty_list[0]))
    l2 = list(range(*duty_list[1]))

    return l1, l2


def file_parser(input_file_name):
    with open(input_file_name) as f:
        cleanup_duties = f.read().split('\n')

    return cleanup_duties


def split_groups(input_group):
    return input_group.split(',')


def generate_range(input_groups):
    g1, g2 = input_groups
    item1, item2 = g1.split('-')
    item3, item4 = g2.split('-')

    return [[int(item1), int(item2) + 1], [int(item3), int(item4) + 1]]
