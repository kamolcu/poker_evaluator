#!/bin/bash
#python -V

python ./poker-evaluator.py
python ./poker-evaluator.py AS,4H,10D,8CKD
python ./poker-evaluator.py dfhaks
python ./poker-evaluator.py AD,4H,10D,8C,KX
python ./poker-evaluator.py AS,4H,10D,8Z,KD
python ./poker-evaluator.py AS,4H,10D,8D,8D
python ./poker-evaluator.py QS,QS,QS,QS,QS
python ./poker-evaluator.py 10S,FH,10D,8D,8C

python ./poker-evaluator.py AS,4H,10D,8C,KD
python ./poker-evaluator.py KS,4H,10D,8C,KD
python ./poker-evaluator.py 4S,4H,10D,6C,2S
python ./poker-evaluator.py 9S,9H,10D,6C,6S
python ./poker-evaluator.py AS,AH,AD,6C,2S
python ./poker-evaluator.py AS,AH,AD,6C,6S
python ./poker-evaluator.py AS,AH,AD,AC,2S
python ./poker-evaluator.py 2S,3H,4D,5C,6S
python ./poker-evaluator.py 10S,AH,QD,KC,JD
python ./poker-evaluator.py KS,KH,KD,KC,JD
python ./poker-evaluator.py 5S,6S,3S,4S,2S
python ./poker-evaluator.py AH,6H,9H,8H,10H
python ./poker-evaluator.py AS,QS,KS,JS,10S
python ./poker-evaluator.py 7C,6C,9C,8C,10C
python ./poker-evaluator.py AD,QD,KD,JD,10D
python ./poker-evaluator.py 2D,2S,4D,5D,6D
python ./poker-evaluator.py 9D,10C,JD,KS,QS

# AS,4H,10D,8C,KD --> AS - High Card
# 4S,4H,10D,6C,2S --> 1 Pair of 4
# 9S,9H,10D,6C,6S --> 2 Pairs of 9 and 6
# AS,AH,AD,6C,2S --> 3 Cards of A
# AS,AH,AD,6C,6S --> 3 Cards of A, 1 Pair of 6 - Full House
# AS,AH,AD,AC,2S --> 4 Cards of A
# 2S,3H,4D,5C,6S --> Straight 2 - 6
# 10S,AH,QD,KC,JD --> Straight 10 - A
# KS,KH,KD,KC,JD --> Four of a kind of K
# 5S,6S,3S,4S,2S --> Straight Flush 2 to 6
# AS,QS,KS,JS,10S --> Royal Straight Flush
