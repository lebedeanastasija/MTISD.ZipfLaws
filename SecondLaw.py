import TextHelper
from WordFrequency import WordFrequency
from RankInfo import RankInfo


class SecondLaw:

    def __init__(self, text,  l_rank, h_rank):
        words = TextHelper.get_words(text)
        # print("All words:")
        # print(words)

        self.filtered_words = TextHelper.filter_words(words)
        # print("Filtered words:")
        # print(self.filtered_words)

        self.words_total = len(self.filtered_words)
        self.low_rank = l_rank
        self.high_rank = h_rank
        self.sorted_counts = []
        self.sorted_frequencies = []
        self.word_frequencies = []
        self.rank_info = []

    def calc_parameters(self):
        self.calc_frequencies()
        self.sort_frequencies()
        self.save_rank_info()
        key_words = []

        print("Max rank: {}".format(len(self.sorted_frequencies)))
        print("Process rank: {}-{}".format(self.low_rank, self.high_rank))

        for x in range(self.low_rank, self.high_rank + 1):
            for rank_word in self.rank_info[x - 1].words:
                key_words.append(rank_word)

        print("Key words: {}".format(', '.join(key_words)))

    def calc_frequencies(self):
        for word in self.filtered_words:
            frequency = self.get_word_frequency(word)
            if frequency is None:
                frequency = WordFrequency(word, self.words_total)
                self.word_frequencies.append(frequency)
            else:
                frequency.add()

    def get_word_frequency(self, word):
        word_frequency = None
        for freq in self.word_frequencies:
            if freq.is_for_word(word):
                word_frequency = freq
        return word_frequency

    def sort_frequencies(self):
        for freq in self.word_frequencies:
            freq_count = freq.get_count()
            if freq_count not in self.sorted_counts:
                self.sorted_counts.append(freq_count)
        self.sorted_counts.sort(reverse=True)
        self.sorted_frequencies = list(map(lambda x: x / self.words_total, self.sorted_counts))

    def save_rank_info(self):
        ranks_count = len(self.sorted_frequencies)
        print("\n>> The 2'nd Zipf Law <<")
        for x in range(ranks_count):
            new_rank = RankInfo(self.sorted_counts[x], self.sorted_frequencies[x], x + 1)
            new_rank.set_words(self.get_words_by_frequency(new_rank.get_count()))
            self.rank_info.append(new_rank)
            print("[{}] p_i={}, r={}, words number: {}".format(
                x, new_rank.frequency, new_rank.rank, len(new_rank.words)
            ))

    def get_words_by_frequency(self, count):
        words_info = list(filter(lambda x: x.has_count(count), self.word_frequencies))
        return list(map(lambda x: x.get_word(), words_info))

    def get_graph_info(self):
        x_vector = []
        y_vector = []
        for item in self.rank_info:
            x_vector.append(item.frequency)
            y_vector.append(len(item.words))
        return [
            x_vector,
            y_vector
        ]