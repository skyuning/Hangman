import re


def guess_next_letter(pattern, used_letters=[], word_list=[]):
    """
    Returns a letter from the alphabet.
    Input parameters:
        pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """

    # filter words match the pattern
    regex = pattern.replace('_', '.')
    full_regex = '^' + regex + '$'
    matched_words = filter(lambda word: re.match(full_regex, word), word_list)
    print(matched_words)

    # calc letter count
    letter_stat = dict()
    max_letter = None
    max_letter_cnt = 0
    for word in matched_words:
        word_len = len(word)
        for i in range(word_len):
            if regex[i] != '.':
                continue
            letter = word[i]
            if letter in letter_stat:
                letter_stat[letter] = letter_stat[letter] + 1
            else:
                letter_stat[letter] = 1

            if max_letter_cnt < letter_stat[letter]:
                max_letter = letter
                max_letter_cnt = letter_stat[letter]

    print(letter_stat)
    print(max_letter)
    return max_letter


def test_function_should_return_something():
    pattern = "acce_t"
    used_letters = list("abcde")
    word_list = ['about', 'abound', 'aboard', 'abroad', 'abrupt',
                 'absent', 'absorb', 'absurd', 'accent', 'accept', 'access']
    assert guess_next_letter(pattern, used_letters, word_list) is not None


test_function_should_return_something()
