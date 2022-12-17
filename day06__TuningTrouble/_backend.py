"""Created on Dec 18 00:11:13 2022."""


def file_parser(input_file):
    with open(input_file, 'r') as f:
        data_stream = f.read().split('\n')

    return data_stream


def check_for_data_marker(input_file):
    data_stream = file_parser(input_file)[0]
    break_ = []
    for i in range(len(data_stream)):
        if len(set(data_stream[i:i + 14])) == len(data_stream[i: i + 14]):
            break_.append(i + 14)

    return break_[0]
