# -*- coding: utf-8 -*-
import sys
import argparse
from sets import Set
import re


def count_pair(sorted_ranks_list):
    ans_map = {}
    for ii in xrange(0, 4):
        first = sorted_ranks_list[ii]
        second = sorted_ranks_list[ii + 1]
        if (first == second):
            if (first not in ans_map):
                ans_map[first] = 2
            else:
                ans_map[first] = ans_map[first] + 1

    pair_ans = []
    triple_ans = []
    four_ans = []
    for key in ans_map.keys():
        if (ans_map[key] == 2):
            pair_ans.append(key)
        elif (ans_map[key] == 3):
            triple_ans.append(key)
        elif (ans_map[key] == 4):
            four_ans.append(key)

    return (pair_ans, triple_ans, four_ans, ans_map)


def is_flush(suit_set):
    if (len(suit_set) == 1): return True
    return False


def is_straight(sorted_ranks_list, ranks_set_len):
    straight = False
    royal = False
    if (len(ranks_set) == 5):
        start = ord(sorted_ranks_list[0])
        end = ord(sorted_ranks_list[-1])
        if ((end - start + 1) == 5):
            straight = True
            if (start == ord(':') and end == ord('>')):
                # start from 10 = royal straight
                royal = True
    return (straight, royal)


def normalize(rank):
    list = {'A': '>', 'K': '=', 'Q': '<', 'J': ';', '10': ':'}
    for key in list.keys():
        if key == rank:
            rank = re.sub(key, list[key], rank)
            break
    return rank


def format_rank(rank):
    list = {'>': 'A', '=': 'K', '<': 'Q', ';': 'J', ':': '10'}
    for key in list.keys():
        if key == rank[0]:
            rank = re.sub(key, list[key], rank)
            break
    return rank

def format_suit(suit):
    list = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
    return list[suit]

def make_output(suit_set, sorted_ranks_list, ranks_set, sorted_rank_suit_list):
    flush = False
    straight = False
    output = 'High Card ' + format_rank(sorted_rank_suit_list[-1])
    flush_suit = next(iter(suit_set))
    if (is_flush(suit_set)):
        flush = True
        output = 'Flush of ' + format_suit(flush_suit)
    (straight, royal) = is_straight(sorted_ranks_list, ranks_set)
    if (flush and straight):
        output = 'Straight ' + output + ' (' + format_rank(sorted_ranks_list[
            0]) + ' to ' + format_rank(sorted_ranks_list[-1]) + ')'
        if (royal):
            output = 'Royal ' + output
        return output
    elif (straight):
        output = 'Straight ' + format_rank(sorted_ranks_list[
            0]) + ' to ' + format_rank(sorted_ranks_list[-1])
        return output
    elif (flush):
        return output

    (pair, triple, four, ans) = count_pair(sorted_ranks_list)
    if (len(pair) > 0):
        pair_str = format_rank(pair[0])
        if (len(pair) == 1):
            if (len(triple) == 0):
                output = 'One pair of ' + pair_str
            elif (len(triple) > 0):
                output = 'Full House (Three of a kind / Pair) = ' + format_rank(
                    triple[0]) + ',' + pair_str
        elif (len(pair) == 2):
            pair2_str = format_rank(pair[1])
            output = 'Two Pairs of ' + pair_str + ' and ' + pair2_str
    elif (len(triple) > 0):
        output = 'Three of a kind of ' + format_rank(triple[0])
    elif (len(four) > 0):
        output = 'Four of a kind of ' + format_rank(four[0])

    return output


parser = argparse.ArgumentParser(description='Poker evaluator script')
parser.add_argument(
    'cards',
    help='Input of 5 cards on hand to be evaluated, separate by comma e.g. AS,4H,10D,8C,KD (S = SPADES, H = HEARTS, D = DIAMONDS, C = CLUBS)')
args = parser.parse_args()

inputs = str.split(args.cards, ',')
if (len(inputs) != 5):
    msg = 'Input --> %s |   Output --> %s' % (
        args.cards.ljust(19), 'Invalid lenght of input. It requires 5 cards.')
    sys.exit(msg)

ranks_list = []
rank_suit_list = []
ranks_set = Set()
suit_set = Set()
cards_set = Set()

for card in inputs:
    suit = card[-1]
    # print('suit = %s' % suit)
    if (not re.match('[shdc]', suit, flags=re.IGNORECASE)):
        msg = 'Input --> %s |   Output --> %s' % (
            args.cards.ljust(19), 'Unknown of suit value ' + suit)
        sys.exit(msg)

    # split rank and suit
    (rank, unused) = re.split('[shdc]', card, flags=re.IGNORECASE)

    if (not re.match('[2-9AKJQ]|10', rank, flags=re.IGNORECASE)):
        msg = 'Input --> %s |   Output --> %s' % (
            args.cards.ljust(19), 'Unknown of rank value ' + rank)
        sys.exit(msg)

    rank = normalize(rank)
    rank_suit_list.append(rank + suit)
    suit_set.add(suit)
    ranks_set.add(rank)
    ranks_list.append(rank)
    cards_set.add(card)

if (len(cards_set) != 5):
    msg = 'Input --> %s |   Output --> %s' % (args.cards.ljust(19),
                                              'Cards must be unique.')
    sys.exit(msg)

rank_suit_list.sort()
ranks_list.sort()
print('Input --> %s |   Output --> %s' %
      (args.cards.ljust(19), make_output(suit_set, ranks_list, ranks_set,
                                         rank_suit_list)))
