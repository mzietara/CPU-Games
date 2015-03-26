# play nim
import random
from nim import *

num_collection = int(raw_input("How many collections? "))
max_size = int(raw_input("Maximum collection size? "))

collections = []
for c in range(num_collection):
    collections.append(random.randint(1, max_size))

g = NimState((list(collections), 'p1'))
print "Game begins in this state: ", str(g)
print "Where the collections index from 0 (leftmost) and you may"
print " reduce to any number from 0 to one less than collection size."

while not (g.winner('p1') or g.winner('p2')):
    if g.player() == 'p1':
        i = int(raw_input("Reduce which collection? "))
        n = int(raw_input("Reduce to what value? "))
        g = g.make_move((i, n))
        print "Game state: ", str(g)
    else: # computer's turn
        m = g.minimax(99999)[0] # best move, look-ahead 1
        print "move: ", m
        g = g.make_move(m)
        print "Game state: ", str(g)

              


