#!/usr/bin/python

'''Simple tools printing candidate words for draw something.'''

import itertools
import sys

LOOKUP = {}

def generate_candidate_sets(chars, length):
    '''
    Returns a set of all signatures of length n possible with characters from char.

    Args:
    chars: A sorted string
    '''

    if length == 0:
        return set([''])

    if len(chars) < length:
        return set()

    candidates = set()

    for i in xrange(len(chars)):
        for candidate in generate_candidate_sets(chars[i+1:], length-1):
            candidates.add(chars[i] + candidate)

    return candidates

def find(chars, length):
    '''
    finds all words of specified length that can be constructed 
    with characters from chars
    '''

    chars = ''.join(sorted(chars))
    cand = generate_candidate_sets(chars, length)
    result = [ LOOKUP[c] for c in cand if c in LOOKUP ]

    return list(itertools.chain(*result))

def init_lookup(fname, length):
    '''Reads the dictionary and finds candidates of the specified length'''
    with open(fname) as file_:
        for word in file_:
            word = word.strip()
            if len(word) != length:
                continue
            sig = ''.join(sorted(word))
            if sig in LOOKUP:
                LOOKUP[sig].append(word)
            else:
                LOOKUP[sig] = [word]

if __name__ == '__main__':

    try:
        LETTERS, LENGTH = sys.argv[1], int(sys.argv[2])
    except (ValueError, IndexError):
        print 'Prints potential words for your game of draw something.'\
            '\n\nUsage:\t%s <characters> <number of letters in result>\n'\
            % sys.argv[0]
        exit()


    init_lookup('/usr/share/dict/words', LENGTH)
    print sorted(find(LETTERS, LENGTH))
    
