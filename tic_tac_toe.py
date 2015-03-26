# tic-tac-toe game
import minimax as mm
import copy
        
class TicTacToe(mm.GameState):

    """Tic-tac-toe GameState.
    """

    def __init__(self, start_state): 
        """Create a tic-tac-toe game in start_state.

           Arguments:
           start_state: A tuple consisting of two elements:
                          --a list of k lists, where each list has k entries,
                            consisting of either None (empty), 'p1' (occupied
                            by player 1), or 'p2' (occupied by player 2), where
                            k is, implicitly, the size of the list
                          --current (to play) player, 'p1' or 'p2'.

            Assumption:
            start_state represents a valid tic-tac-toe game.

           Returns:
           A tic-tac-toe game in start_state.
        """
        
        mm.GameState.__init__(self, start_state)

    def winner(self, player):
        """Return whether player has won.

           Arguments:
           Player may be either the current player or the opponent.

           Assumptions:
           Only one of p1 or p2 may be the winner.

           Returns
           Exactly one of True or False
        """
        
        p_win = [player] * len(self._state[0])
            
        #Check the columns and diagonals for a win. There will always be two
        #diagonals.
        diag_1 = []
        diag_2 = []
        
        for c in range(len(self._state[0])):
            
            diag_1.append(self._state[0][c][c])
            diag_2.append(self._state[0][c][len(self._state[0]) - 1 - c])
            
            #Check the rows for a win
            if self._state[0][c] == p_win:
                return True
            
            column = []
            for r in range(len(self._state[0])):
                column.append(self._state[0][r][c])
                
            if column == p_win:
                return True

        if diag_1 == p_win or diag_2 == p_win:
            return True
        
        return False

    def __str__(self):
        '''String representation of board.
           
           Returns
           A string where the first line reads 'To play: p?\n'
           where p? is the current player,
           followed by a \n-terminated line for each row, where each
           instance of p1 is replaced by X, each p2 is replaced by O,
           and each None is replaced by -
        '''
        
        result = "To play: %s\n" % (self.player())
        for row in self._state[0]:
            for spot in row:
                if spot == 'p1':
                    result += "X"
                elif spot == 'p2':
                    result += 'O'
                else:
                    result += "-"
                #result += "   "
            result += '\n'
        
        return result

    def next_move(self):
        """Return a (possibly empty) list of legal moves for current player.

            Assumptions:
            The list will be empty if either player has already won, and
            the order of moves in the list is not significant

            Returns:
            A list of pairs of legal moves of the form (r, c) such that
            self._state[0][r][c] is currently unoccupied and the current player
            may move by occupying it.
        """
        
        moves = []
        if self.winner(self.player()) or self.winner(self.opponent()):
            return moves
        for r in range(len(self._state[0])):
            for c in range(len(self._state[0][r])):
                if self._state[0][r][c] == None:
                    moves.append((r, c))
        return moves

    def make_move(self, move):
        """Apply move to current game.

           Arguments:
           move:  A pair (r, c) representing square self._state[0][r][c]

           Assumptions:
           (r, c) are valid coordinates for self._state[0].  If they represent
           a valid move for current player, then the current player occupies
           that position and the opponent becomes the current player.
           Otherwise self._state is left unchanged.

           Returns:
           New game with move appended to self._state[0] and current player
           replaced by opponent, if this is legal.  Otherwise return None.
        """
        r, c = move[0], move[1]
        if self._state[0][r][c] == None:
            state = copy.deepcopy(self._state[0])
            state[r][c] = self.player()
            return TicTacToe((state, self.opponent()))

    def heuristic_eval(self):
        """Return number of opportunities open to this player, minus those
           open to opponent.  A row, column, or diagonal is an open
           opportunity if it has no squares occupied by this player's
           opponent.

           Assumptions:
           The evaluation is not exact, and is, in general, inferior to an
           exact evaluation.

           Returns:
           Number of rows, columns, diagonals open to this player, minus
           those open to opponent, divided by total possible winning lines.
        """
        
        #count the player's and opponent's opportunities, respectively.
        p_count, opp_count = 0, 0
        
        blank_line = [None] * len(self._state[0])
        
        #count the total number of winning lines. This is the current player's
        #opportunities added to the opposing player's opportunities, subtracted
        #by any opportunities that the players have in common, which will be
        #lines that contain only None. Subtract all of the lines in common
        #first, then add p_count and opp_count once the counting is finished.
        total_count = 0
            
        #Check the columns and diagonals for opportunities
        diag_1 = []
        diag_2 = []
        
        for c in range(len(self._state[0])):
            
            diag_1.append(self._state[0][c][c])
            diag_2.append(self._state[0][c][len(self._state[0]) - 1 - c])
            
            #Check the rows for opportunities
            if self.opponent() not in self._state[0][c]:
                p_count += 1
            if self.player() not in self._state[0][c]:
                opp_count += 1
            if self._state[0][c] == blank_line:
                total_count -= 1
            
            column = []
            for r in range(len(self._state[0])):
                column.append(self._state[0][r][c])
                
            if self.opponent() not in column:
                p_count += 1
            if self.player() not in column:
                opp_count += 1
            if column == blank_line:
                total_count -= 1

        if self.opponent() not in diag_1:
            p_count += 1
        if self.player() not in diag_1:
            opp_count += 1
        if diag_1 == blank_line:
                total_count -= 1
            
        if self.opponent() not in diag_2:
            p_count += 1
        if self.player() not in diag_2:
            opp_count += 1
        if diag_2 == blank_line:
                total_count -= 1
                
        total_count += p_count + opp_count
        if total_count == 0:
            return 0

        return (p_count - opp_count) * 1.0 / total_count
