# test tic_tac_toe
import unittest
import tic_tac_toe

#inf = float('inf')
#Change this back after.
inf = float(1e100000000)

class TicTacToeTest(unittest.TestCase):

    '''Test tic-tac-toe GameState implementation.'''

    def test_win_row(self):
        '''Test whether a winning row detected.'''

        r1 = [None, None, None]
        r2 = ['p1', 'p1', 'p1']
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertTrue(ttt.winner('p1'))

    def test_win_column(self):
        '''Test whether a winning column detected.'''

        r1 = [None, 'p1', None]
        r2 = [None, 'p1', None]
        r3 = [None, 'p1', None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertTrue(ttt.winner('p1'))

    def test_win_diag(self):
        '''Test whether winning top-left -> bottom-right diagonal detected.'''

        r1 = ['p1', None, None]
        r2 = [None, 'p1', None]
        r3 = [None, None, 'p1']
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertTrue(ttt.winner('p1'))

    def test_win_anti_diag(self):
        '''Test whether winning bottom-left -> top-right diagonal detected.'''

        r1 = [None, None, 'p1']
        r2 = [None, 'p1', None]
        r3 = ['p1', None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertTrue(ttt.winner('p1'))

    def test_str(self):
        '''Test string method.'''

        r1 = ['p1', None, 'p1']
        r2 = [None, 'p2', 'p2']
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.__str__(),
                        "To play: p1\nX-X\n-OO\n---\n")

    def test_next_move_non_empty(self):
        '''Test whether expected move list generated.'''

        r1 = ['p1', None, 'p1']
        r2 = [None, 'p2', 'p2']
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        moves = ttt.next_move()
        moves.sort()
        self.assertEqual(moves, [(0, 1), (1, 0), (2, 0), (2, 1), (2, 2)])
        
    def test_next_move_after_win(self):
        '''Test that no moves listed after game won.'''

        r1 = ['p1', None, None]
        r2 = ['p1', None, 'p2']
        r3 = ['p1', None, 'p2']
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertTrue(len(ttt.next_move()) == 0)

    def test_next_move_cats_game(self):
        '''Test that no moves listed after game tied.'''

        r1 = ['p1', 'p2', 'p1']
        r2 = ['p2', 'p1', 'p2']
        r3 = ['p1', 'p2', 'p1']
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertTrue(len(ttt.next_move()) == 0)

    def test_make_move_occupied(self):
        '''Test that move into occupied space not allowed.'''

        r1 = ['p1', None, None]
        r2 = ['p1', None, 'p2']
        r3 = ['p1', None, 'p2']
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        g = ttt.make_move((1, 0))
        self.assertTrue(not g)  # g is None

    def test_minimax_p1_draw_blank(self):
        '''Test that p1 expects draw at outset.'''

        r1 = [None, None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p2_draw_blank(self):
        '''Test that p2 expects draw at outset.'''

        r1 = [None, None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p2_draw_corner(self):
        '''Test that p2 expects draw when p1 takes corner.'''

        r1 = ['p1', None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p2_draw_side(self):
        '''Test that p2 expects draw when p1 starts on side.'''
        r1 = [None, 'p1', None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p2_draw_centre(self):
        '''Test that p2 expects a draw when p1 starts in centre.'''

        r1 = [None, None, None]
        r2 = [None, 'p1', None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p1_draw_m2(self):
        '''Test that p1 expects a draw after corner and p2 plays centre.'''

        r1 = ['p1', None, None]
        r2 = [None, 'p2', None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)
        
    def test_minimax_p2_draw_m2(self):
        '''Test that p2 expects a draw after corner, p1 plays centre.'''

        r1 = ['p2', None, None]
        r2 = [None, 'p1', None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p2'))
        self.assertEqual(ttt.minimax(inf)[1],
                         0)

    def test_minimax_p1_win_p2_near_side(self):
        '''Test that p1 expects to win after corner, p2 plays adjacent'''

        r1 = ['p1', 'p2', None]
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         1)

    def test_minimax_p1_win_p2_far_side(self):
        '''Test that p1 expects win after corner, p2 non-adjacent side.'''

        r1 = ['p1', None, None]
        r2 = [None, None, 'p2']
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         1)

    def test_minimax_p1_win_p2_near_corner(self):
        '''Test that p1 expects win after corner, p2 adjacent corner.'''

        r1 = ['p1', None, 'p2']
        r2 = [None, None, None]
        r3 = [None, None, None]
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         1)

    def test_minimax_p1_win_p2_far_corner(self):
        '''Test that p1 expects win after corner, p2 opposite corner.'''

        r1 = ['p1', None, None]
        r2 = [None, None, None]
        r3 = [None, None, 'p2']
        ttt = tic_tac_toe.TicTacToe(([r1, r2, r3], 'p1'))
        self.assertEqual(ttt.minimax(inf)[1],
                         1)

suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
unittest.TextTestRunner(verbosity=2).run(suite)
