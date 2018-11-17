class RankInfo:
    def __init__(self, count, frequency, rank):
        self.count = count
        self.frequency = frequency
        self.rank = rank
        self.words = []

    def get_count(self):
        return self.count

    def get_frequency(self):
        return self.frequency

    def has_rank(self, rank):
        return self.rank == rank

    def set_words(self, words):
        self.words = words
