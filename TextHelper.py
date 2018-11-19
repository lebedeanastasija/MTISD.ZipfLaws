import codecs
import re

ru_filter = [
    "без", "вне", "для", "изо", "меж", "над", "обо", "ото", "под", "при", "про",
    "она", "оно", "они",
    "мой", "ваш", "наш", "его", "тот", "сей",
    "сам", "свой", "сама", "сами", "само", "себя",
    "это", "вот", "тут", "той", "эти", "этот", "который", "которая", "которое", "которые", "которых", "которому", "тому",
    "много", "немного", "мало", "каждый", "каждой", "больше", "меньше",
    "когда", "кто", "что", "чей", "где",
    "как", "так", "еще", "все", "ибо", "или", "тем", "чем", "тех",
    "снова", "опять", "часто", "редко", "после",
    "однако", "очевидно", "также", "чтобы",
    "был", "была", "было", "были", "будет", "будут", "стал", "стала", "стало", "стали"
]

en_filter = [
    "the", "for", "and", "but", "with", "about", "from",
    "that", "this", "here",
    "how", "who", "where", "what", "whose", "why", "which",
    "some", "same", "any", "not", "more", "less", "only", "just", "also", "all", "one", "everything", "nothing", "many", "very",
    "you", "your", "yours", "she", "her", "his", "our", "they", "their", "its", "them",
    "should", "must", "would", "have", "has", "had", "will", "are", "were", "was", "can", "cannot", "could", "lets"
]


def get_words(text_string):
    row_lines = text_string.splitlines()

    lines = list(filter(lambda l: len(l) > 0, row_lines))
    lines = list(map(lambda l: re.sub("[,.!?0-9:;=&^%$#@*+’'{}()[\]«»“”°×]", "", l), lines))
    lines = list(map(lambda l: re.sub("^(\s+)", "", l), lines))
    lines = list(map(lambda l: re.sub("(\s+)$", "", l), lines))
    lines = list(map(lambda l: re.sub("-", " ", l), lines))
    lines = list(map(lambda l: re.sub("—", " ", l), lines))
    lines = list(map(lambda l: re.sub("/", " ", l), lines))
    lines = list(map(lambda l: re.sub("\s\s+", " ", l), lines))

    prepared_string = ' '.join(lines).lower()
    words = prepared_string.split()
    return words


def filter_words(words):
    words = list(filter(lambda x: len(x) > 2, words))
    words = list(filter(lambda x: x not in ru_filter, words))
    words = list(filter(lambda x: x not in en_filter, words))
    return words


def get_texts(files):
    texts = []
    for file in files:
        texts.append(get_text(file))
    return texts


def get_text(file):
    file_obj = codecs.open(file, "r", "utf_8_sig")
    file_text = file_obj.read()
    file_obj.close()
    return file_text

