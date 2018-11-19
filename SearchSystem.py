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

        print("SEARCH RESULT:")
        print("query key words >>")
        print(self.query_key_words)
        print("articles key words >>")
        for items in self.articles_key_words:
            print(items)

    def get_query_key_words(self):
        second_law = SecondLaw(self.query)
        second_law.calc_parameters()
        self.query_key_words = second_law.key_words

    def get_articles_key_words(self):
        print("Analyzing files: ")
        self.article_texts = TextHelper.get_texts(self.article_names)

        weights_method = WeightsMethod(self.article_texts, 1)
        self.articles_key_words = weights_method.get_key_words()



