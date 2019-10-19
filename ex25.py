"""Exercise 25."""


def break_words(stuff):
    """Break Words."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sort Words."""
    return sorted(words)


def print_first_word(words):
    """Print First Word."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Print Last Word."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Sort Sentence."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Print First and Last."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Print First and Last Sorted."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
