'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # for word sizes that can't possibly hold 'th'
    if len(word) <= 2 and word != 'th':
        return 0
    # base case: word contains "th" we find a match
    elif word == 'th':
        return 1
    # recurse looking at first two letters then moving down the string by letter
    else:
        return count_th(word[:2])+count_th(word[1:])
