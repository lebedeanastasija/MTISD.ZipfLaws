import codecs

import TextHelper
from WeightsMethod import WeightsMethod
from SecondLaw import SecondLaw


def get_file_text(path):
    file_obj = codecs.open(path, "r", "utf_8_sig")
    file_text = file_obj.read()
    file_obj.close()
    return file_text


class SearchSystem:

    def __init__(self, query, article_names):
        self.query = query
        self.article_names = article_names
        self.article_texts = []
        self.query_key_words = None
        self.articles_key_words = None

    def search_article(self):
        self.get_query_key_words()
        self.get_articles_key_words()

        article_index = self.find_proper_article()
        article_name = self.article_names[article_index]
        article_key_words = self.articles_key_words[article_index]

        print('Result article: {}'.format(article_name))
        print("query key words: {}".format(', '.join(self.query_key_words)))
        print("articles key words: {}".format(', '.join(article_key_words)))

    def get_query_key_words(self):
        second_law = SecondLaw(self.query)
        second_law.calc_parameters()
        self.query_key_words = second_law.get_key_words()

    def get_articles_key_words(self):
        print("Analyzing files: ")
        self.article_texts = TextHelper.get_texts(self.article_names)

        weights_method = WeightsMethod(self.article_texts, 1)
        self.articles_key_words = weights_method.get_key_words(False)

    def find_proper_article(self):
        articles_fitness = []
        articles_total = len(self.article_names)
        article_index = 0

        for x in range(articles_total):
            fitness = 0

            for word in self.articles_key_words[x]:
                if word in self.query_key_words:
                    fitness = fitness + 1
            articles_fitness.append(fitness)

            if x != 0:
                if fitness > articles_fitness[article_index]:
                    article_index = x

        return article_index


