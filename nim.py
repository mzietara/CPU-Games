# implement a nim variant

import minimax as mm
import copy

class NimState(mm.GameState):
    """Normal play state of game nim.

       Assumptions:
       Play begins with collections of tokens. Two players alternate plies.
       In each ply a player removes a positive number of tokens from exactly
       one of the collections.  The player to remove the last token(s) wins.
    """

    def __init__(self, start_state):
        """Create a nim game in start_state.

           Arguments:
           start_state: a pair consisting of a tuple of positive integers
                        representing collection sizes, and the current
                        (to play) player, one of 'p1' or 'p2'.

           Returns:
           A nim game state in start_state.
        """

        mm.GameState.__init__(self, start_state)

    def winner(self, player):
        """Return whether player has won this ply.

           Assumptions:
           Play ends as soon as the current player (the loser) is unable to
           remove more tokens.

           Returns:
           True if player has won, and hence the current player has lost.
        """

        for c in self._state[0]:
            if c > 0:
                return False # GameState not over
        else:
            return player == self.opponent() # current player lost
    
    def __str__(self):
        """Return a string representing the current nim ply.

           Returns
           The current (to play) player and the list of collection
           size(s).
        """

        s = "To play: " + self._state[1] + "\nCollections: "
        for c in self._state[0]:
            s = s + str(c) + " "
        return s + "\n"

    def next_move(self):
        """Return a (possibly empty) list of moves available to current player.

           Assumptions:
           Collections contain zero or more tokens, and a legal move removes
           one or more tokens from exactly one of the collections, leaving
           a strictly smaller collection.

           Returns:
           A list of all possible pairs of the form (i, n) where n is a
           non-negative integer smaller than the size of the collection at
           index i.
        """

        move_list = [] # empty list to start
        for i in range(len(self._state[0])):
            for n in range(self._state[0][i]):
                move_list.append((i, n))
        return move_list

    def make_move(self, move):
        """Apply move to current game state.

           Arguments:
           move: A pair(i, n), where n is a non-negative integer smaller than
           the size of the collection at index i.

           Returns:
           A new NimState with player self.opponent() and self._state[0][i] replaced
           by n.
        """

        state = list(copy.deepcopy(self._state[0]))
        state[move[0]] = move[1]
        return NimState((tuple(state), self.opponent()))

    def heuristic_eval(self):
        """Return WIN if current player faces a positive nim-sum,
        LOSE otherwise.
        

           Assumption:
           Current player is in a winning position if the nim-sum of the
           collections is positive, and a losing position if the nim-sum
           of the collections is zero.  There are no draws.  This is a special
           case: an exact heuristic is known for nim.
        """
        
        nim_sum = 0
        for c in self._state[0]:
            nim_sum = nim_sum ^ c  # take the XOR
        if nim_sum > 0:
            return self.WIN
        else:
            return self.LOSE
