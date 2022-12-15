from lib import is_match
from lib.error import EndsWithInvalidWordException

text_history = []

def pop_right():
    text_history.pop(len(text_history) - 1)

def clear():
    text_history.clear()

def append(val):
    text_history.append(val)

def to_list():
    return text_history

def is_empty():
    return len(text_history) == 0

def filter_until_alphabet():
    if len(text_history) == 0: return []
    hist = [*text_history]
    while len(hist) > 0 and not hist[len(hist) - 1].isalpha():
        hist.pop(len(hist) - 1)
    return hist

def ends_with_되():
    word_list = filter_until_alphabet()
    if len(word_list) < 3: return

    last_three = word_list[len(word_list) - 3 : len(word_list)]
    되_cases = [['ㄷ', "ㅗ", "ㅣ"], ['e', "h", "l"], ['E', "H", "L"]]
    for 되_case in 되_cases:
        if is_match(last_three, 되_case):
            return True

def validate():
    if ends_with_되():
        text_history.clear()
        raise EndsWithInvalidWordException("되")