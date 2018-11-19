import os
import codecs
from matplotlib import pyplot

from FirstLaw import FirstLaw
from SecondLaw import SecondLaw
from WeightsMethod import WeightsMethod
from SearchSystem import SearchSystem


def display_title_bar():
    os.system('cls')

    print("\n**********************************************")
    print("***************** Zipf Laws ******************")
    print("**********************************************")


def quit():
    print("\nThanks for your work!")


def get_user_choice():
    print("[1] Define article key words.")
    print("[2] Search article by query.")
    print("[q] Quit.")

    return input("What would you like to do? ")


def show_available_articles():
    print("\nSelect one of the following Articles:")
    i = 0
    for text in texts:
        i += 1
        print("[" + str(i) + "] " + text)
    print("[m] Menu")
    return input("Your choice: ")


def show_available_topics():
    print("\nSearch text article for one of the following topics:")
    i = 0
    for topic in topics:
        i += 1
        print("[" + str(i) + "] " + topic)


def show_enter_search_query():
    return input("\nEnter search query (one or more words): ")


def draw_graphic(x_vector, y_vector):
    pyplot.plot(x_vector, y_vector)
    pyplot.show()


def get_file_text(path):
    file_obj = codecs.open(path, "r", "utf_8_sig")
    file_text = file_obj.read()
    file_obj.close()
    return file_text


def find_key_words():
    article = show_available_articles()
    if article == 'm':
        display_title_bar()
    else:
        file_path = diff_texts_path + texts[int(article)-1]
        print("File path: " + file_path)
        file_obj = codecs.open(file_path, "r", "utf_8_sig")
        file_text = file_obj.read()
        file_obj.close()

        first_law = FirstLaw(file_text)
        first_law.calc_parameters()
        info = first_law.get_graph_info()
        draw_graphic(info[0], info[1])

        second_low = SecondLaw(file_text, 3, 6)
        second_low.calc_parameters()
        info = second_low.get_graph_info()
        draw_graphic(info[0], info[1])

        print('\n>> Weights Method <<')
        print("Analyzing files: ")
        directory_texts = []
        for text_path in texts:
            file_path = diff_texts_path + text_path
            print(file_path)
            directory_texts.append(get_file_text(file_path))

        weights_method = WeightsMethod(directory_texts, 1)
        print(weights_method.get_key_words())


def search_article():
    show_available_topics()

    query = show_enter_search_query()
    if query == 'm':
        display_title_bar()
    else:
        search_system = SearchSystem(query)
        text = search_system.search_article()


texts = [
    'moon_en.txt',
    'moon_ru.txt',
    'gymnastics_en.txt',
    'gymnastics_ru.txt',
    'female_nutrition_en.txt',
    'female_nutrition_ru.txt'
]


topics = [
    'astronomy',
    'healthy_lifestyle',
    'olympic_games'
]

diff_texts_path = '.\data\diff_texts\\'
topic_texts_path = '.\data'


def main():
    # draw_graphic([x for x in range(10)])

    choice = ''
    article = ''
    topic = ''

    while choice != 'q':
        display_title_bar()
        choice = get_user_choice()

        if choice == '1':
            find_key_words()

        elif choice == '2':
            search_article()

        elif choice == 'q':
            quit()


if __name__ == '__main__':
    main()
