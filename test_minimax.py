# test minimax module
import unittest
import minimax as mm

class TestMinimaxGameState(unittest.TestCase):
    
    '''Pyunit tests for GameState superclass.'''

    def test_opponent(self):
        '''Return whether players have correct opponent'''
        g = mm.GameState(((), 'p1'))
        self.assertEqual(g.opponent(), 'p2')
        g = mm.GameState(((), 'p2'))
        self.assertEqual(g.opponent(), 'p1')

    def test_player(self):
        '''Return whether player is correct.'''
        
        g = mm.GameState(((), 'p1'))
        self.assertEqual(g.player(), 'p1')
        g = mm.GameState(((), 'p2'))
        self.assertEqual(g.player(), 'p2')

suite = unittest.TestLoader().loadTestsFromTestCase(TestMinimaxGameState)
unittest.TextTestRunner(verbosity=2).run(suite)
