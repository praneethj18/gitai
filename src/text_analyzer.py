from collections import Counter
import re

def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def sentence_count(text):
    return len(re.findall(r"[.!?]",text))

def unique_word_count(text):
    words=[word.lower().strip(".,!?") for word in text.split()]
    return len(set(words))

def most_common_word(text):
    words=[word.lower().strip(".,!?") for word in text.split()]
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]