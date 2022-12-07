"""Created on Dec 07 01:43:22 2022."""


class RockPaperScissors:

    def __init__(self, strategy_list):
        with open(strategy_list) as f:
            self.st_list = f.read()

        self.paper_score = 2
        self.rock_score = 1
        self.scissor_score = 3

        self.win_score = 6
        self.draw_score = 3
        self.lose_score = 0

    @staticmethod
    def winning_pair():
        return [['A', 'Y'], ['B', 'Z'], ['C', 'X']]

    @staticmethod
    def draw_paris():
        return [['A', 'X'], ['B', 'Y'], ['C', 'Z']]

    @staticmethod
    def lose_pairs():
        return [['B', 'X'], ['A', 'Z'], ['C', 'Y']]

    # def list_parser(self):
    #     win_pairs = self.winning_pair()
    #     draw_pairs = self.draw_paris()
    #     lose_pairs = self.lose_pairs()
    #
    #     list_ = self.get_list()
    #
    #     total = []
    #
    #     for i in list_:
    #         score = [2 if i[1] == 'Y' else 1 if i[1] == 'X' else 3]
    #         if i in win_pairs:
    #             score.append(6)
    #         elif i in draw_pairs:
    #             score.append(3)
    #         elif i in lose_pairs:
    #             score.append(0)
    #         total.append(sum(score))
    #
    #     return sum(total)

    def list_parser(self):
        win_pairs = self.winning_pair()
        draw_pairs = self.draw_paris()
        lose_pairs = self.lose_pairs()

        list_ = self.get_list()

        total = []

        for i in list_:
            if i[1] == 'Y':
                for pair in draw_pairs:
                    if pair[0] == i[0]:
                        score = [2 if pair[1] == 'Y' else 1 if pair[1] == 'X' else 3, 3]
            elif i[1] == 'X':
                for pair in lose_pairs:
                    if pair[0] == i[0]:
                        score = [2 if pair[1] == 'Y' else 1 if pair[1] == 'X' else 3, 0]
            elif i[1] == 'Z':
                for pair in win_pairs:
                    if pair[0] == i[0]:
                        score = [2 if pair[1] == 'Y' else 1 if pair[1] == 'X' else 3, 6]

            total.append(sum(score))

        return sum(total)

    def get_list(self):
        return [i.split() for i in self.st_list.split('\n')]
