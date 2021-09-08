

class Card():
    def __init__(self, rank='A', suite='S'):
        self.rank = rank
        self.suite = suite

    def get_rank(self):
        return self.rank

    def get_suite(self):
        return self.suite
