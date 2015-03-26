# tools for minimax

def _switch_rate(r):
    '''Return opposing players rating corresponding to r.'''

    return r * -1 # one's loss is the other's gain

def include_better_move(L, ply):
    '''L is a list of tuples that have the first element being the move, and
    the second element is the predicted score of that move. Ply is also a tuple
    of this form. Change L so that if the move of ply is in L, find out which
    one has the better score and replace that element with ply if ply has the
    better score.'''
    
    for i in range(len(L)):
        if L[i][0] == ply[0] and L[i][1] <= ply[1]:
            L[i] = ply
    else:
        L.append(ply)
        
class GameState:
    
    """State of a two-person game, including player about to play.

       Assumptions:
       Two-person, zero-sum game, with exactly three outcomes:
       player one can win, lose, or draw, whereas player two
       can (respectively) lose, win, or draw.
       Each ply toggles player_1 <-> player_2.
    """
    '''Class constants.'''
    WIN = 1
    LOSE = -1
    DRAW = 0
    INF = 999999999999999

    def __init__(self, start_state):
        """Create a new Game in starting state.

            Arguments
            start_state:  Tuple (layout, starting player).
        """
        
        self._state = start_state

    def terminal_eval(self):
        """Return current player's score at end of game.

           Assumptions:
           The game is in a state reachable from the initial position by a
           sequence of plies, with a current player to play, but no further
           plies allowed.

           Returns:
           Return whether the current player wins, loses, or ties.
        """

        if self.winner(self.player()):
            return self.WIN
        elif self.winner(self.opponent()):
            return self.LOSE
        else:
            return self.DRAW

    def heuristic_eval(self):
        """Return estimate of current player's score at end of game.

           Assumptions:
           Game is in a state reachable from initial position by sequence
           of plies, current player to play, possibly further moves allowed.

           Returns:
           Confidence that current player wins (0,1], loses [-1,0), or
           draws (0).
        """
        
        raise NotImplementedError('Implemented in GameState subclass')

    def minimax(self, foresight, pred_max=-1, layout={}):
        """Return best move and score for current GameState.

           Arguments:
           foresight: Number of plies we may look ahead.
           pred_max:  Best score so far of predecessor GameState.
           layout:    Dictionary containing best score and move
                      for each layout
           
            Assumptions:
            Current player has at least one legal move available.

            Returns (m, s)
            s:  Highest score that current player can guarantee.
            m:  Next move that allows current player to guarantee s.
        """
        
        legal_moves = self.next_move()
        all_scores = []
        
        for move in legal_moves:
            #Create a new GameState with the same layout as the current
            #GameState, but with the current move added onto the layout.
            #Keep in mind that when make_move is applied, the current player
            #becomes the opponent.
            new_gs = self.make_move(move)
            if str(new_gs._state) in layout:
                all_scores.append(layout[str(new_gs._state)])

            elif new_gs.winner(new_gs.player()) or \
               new_gs.winner(new_gs.opponent()) or \
               len(new_gs.next_move()) == 0:
                #Since it is the opponent's turn, switch the rate when
                #inputting the score of the current player.
                ms = (move, _switch_rate(new_gs.terminal_eval()))
                all_scores.append(ms)
                
                if new_gs.winner(new_gs.opponent()):
                    pred_max = 1
                    return ms
                
            elif foresight == 0:
                #Can't take any more plies, so estimate the score with
                #heuristic evaluation, and switch the rate.
                ms = (move, _switch_rate(new_gs.heuristic_eval()))
                all_scores.append(ms)
            else:
                current = new_gs.minimax(foresight - 1, pred_max, layout)
                value = (move, _switch_rate(current[1]))
                all_scores.append(value)
                layout[str(new_gs._state)] = value
                
                if value[1] == 1:
                    return (current[0], _switch_rate(current[1]))
                
        #get the highest score from all_scores
        result = all_scores[0]
        for value in all_scores:
            if value[1] >= result[1]:
                result = value
        
        return result

    def player(self):
        """Return current player --- the one with option of moving.

           Assumptions
           Player returned is one of 'p1' or 'p2'.
           Player returned might have no legal moves available.
        """

        return self._state[1]  # state is a 2-tuple 
    
    def opponent(self):
        """Return opponent of current player."""
        if self.player() == 'p1':
            return 'p2'
        else:
            return 'p1'

    def next_move(self):
        """Return a sequence of all legal moves."""
        raise NotImplementedError('Implement next_move in GameState subclass')

    def winner(self, player):
        """Return whether this player has won."""
        raise NotImplementedError('Implement winner in GameState subclass')

    def make_move(self, move):
        """Return new GameState by applying move."""
        raise NotImplementedError('Implement make_move in GameState subclass')
