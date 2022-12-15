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

def filter_until_alphabet(word_list):
    if len(word_list) == 0: return []
    hist = [*word_list]
    while len(hist) > 0 and not hist[len(hist) - 1].isalpha():
        hist.pop(len(hist) - 1)
    return hist

def ends_with_되(word_list):
    _word_list = filter_until_alphabet(word_list)
    if len(_word_list) < 3: return

    last_three = _word_list[len(_word_list) - 3 : len(_word_list)]
    되_cases = [['ㄷ', "ㅗ", "ㅣ"], ['e', "h", "l"], ['E', "H", "L"]]
    for 되_case in 되_cases:
        if is_match(last_three, 되_case):
            return True

def chunk_word_list(word_list, splitter=" "):
    chunks=[]
    cur = []
    for i in range(len(word_list)):
        if word_list[i] == splitter:
            chunks.append([*cur])
            cur = []
        else:
            cur.append(word_list[i])
    if len(cur) > 0:
        chunks.append([*cur])
    return chunks

def validate():
    print(text_history)
    for chunks in chunk_word_list(text_history, " "):
        print(chunks)
        if ends_with_되(chunks):
            text_history.clear()
            raise EndsWithInvalidWordException("되")