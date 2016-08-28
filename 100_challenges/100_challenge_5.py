import re

strs = "I am an NLPer"


def bigram(strs):
    words = strs.split(' ')
    letters = ''.join(strs.split(' '))

    for ind, letter in enumerate(letters):
        if ind < len(letters) - 1:
            print(letter, letters[ind + 1])

    for ind, word in enumerate(words):
        if ind < len(words) - 1:
            print(word, words[ind + 1])

bigram(strs)
