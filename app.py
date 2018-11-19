import os
import codecs
from matplotlib import pyplot

import TextHelper
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
    for text in diff_articles:
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


def find_key_words():
    article = show_available_articles()
    if article == 'm':
        display_title_bar()
    else:
        file_path = diff_articles[int(article)-1]
        print("File path: " + file_path)
        file_text = TextHelper.get_text(file_path)

        first_law = FirstLaw(file_text)
        first_law.calc_parameters()
        info = first_law.get_graph_info()
        draw_graphic(info[0], info[1])

        second_low = SecondLaw(file_text)
        second_low.calc_parameters()
        info = second_low.get_graph_info()
        draw_graphic(info[0], info[1])

        print('\n>> Weights Method <<')
        directory_texts = TextHelper.get_texts(diff_articles)
        weights_method = WeightsMethod(directory_texts, 1)
        print(weights_method.get_key_words())


def search_article():
    show_available_topics()

    query = show_enter_search_query()
    if query == 'm':
        display_title_bar()
    else:
        search_system = SearchSystem(query, topic_articles)
        text = search_system.search_article()


diff_articles = [
    '.\data\diff_texts\\moon_en.txt',
    '.\data\diff_texts\\moon_ru.txt',
    '.\data\diff_texts\\gymnastics_en.txt',
    '.\data\diff_texts\\gymnastics_ru.txt',
    '.\data\diff_texts\\female_nutrition_en.txt',
    '.\data\diff_texts\\female_nutrition_ru.txt'
]

topic_articles = [
    '.\data\\astronomy\\en\\mars.txt',
    '.\data\\astronomy\\ru\\mars.txt',
    '.\data\\astronomy\\en\\moon.txt',
    '.\data\\astronomy\\ru\\moon.txt',
    '.\data\\astronomy\\en\\planetary_system.txt',
    '.\data\\astronomy\\ru\\planetary_system.txt',

    '.\data\\healthy_lifestyle\\en\\female_nutrition.txt',
    '.\data\\healthy_lifestyle\\ru\\female_nutrition.txt',
    '.\data\\healthy_lifestyle\\en\\office_physical_culture.txt',
    '.\data\\healthy_lifestyle\\ru\\office_physical_culture.txt',

    '.\data\\olympic_games\\en\\gymnastics.txt',
    '.\data\\olympic_games\\ru\\gymnastics.txt',
    '.\data\\olympic_games\\en\\modern_olympic_games.txt',
    '.\data\\olympic_games\\ru\\modern_olympic_games.txt',
    '.\data\\olympic_games\\en\\table_tennis.txt',
    '.\data\\olympic_games\\ru\\table_tennis.txt'
]


topics = [
    'astronomy',
    'healthy_lifestyle',
    'olympic_games'
]

diff_texts_path = '.\data\diff_texts\\'


def main():

    choice = ''

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
