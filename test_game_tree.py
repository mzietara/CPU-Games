# test game_tree module
import unittest
import game_tree
import tic_tac_toe

class TestNearlyFull(unittest.TestCase):

    '''Unit tests for GameStateNode using nearly-full TicTacToe'''
    
    def setUp(self):
        '''Create a GameStateNode.'''

        self.node = game_tree.GameStateNode(tic_tac_toe.TicTacToe(
            ([['p1', 'p2', 'p1'], ['p2', 'p1', 'p2'], ['p2', 'p1', None]],
             'p1')))

    def tearDown(self):
        '''Clean up.'''

        self.node = None

    def testGrow(self):
        '''Should have one child, a leaf.'''
        
        self.node.grow()
        self.assertTrue(len(self.node.children) == 1)
        self.assertTrue(len(self.node.children[0].children) == 0)

    def testNodeCount(self):
        '''Test to see it grows to two nodes.'''

        self.node.grow()
        self.assertTrue(game_tree.node_count(self.node) == 2)

    def testLeafCount(self):
        '''Test to see it grows one leaf.'''

        self.node.grow()
        self.assertTrue(game_tree.leaf_count(self.node) == 1)

class TestEmpty(unittest.TestCase):

    '''Unit tests for GameStateNode using empty TicTacToe.'''

    def setUp(self):
        '''Create a GameStateNode.'''

        self.node = game_tree.GameStateNode(tic_tac_toe.TicTacToe(
            ([[None, None, None], [None, None, None], [None, None, None]],
             'p1')))

    def tearDown(self):
        '''Clean up.'''

        self.node = None

    def testNodeCountLeafCount(self):
        '''Test to see if it grows to 255168 leaf nodes, consistent with
           http://en.wikipedia.org/wiki/Game_complexity#Example:_tic-tac-toe
        '''
        
        self.node.grow() # could take a while, well over a minute
        self.assertTrue(game_tree.leaf_count(self.node) == 255168)

    def testDistinctNodeCountLeafCount(self):
        '''Test to see if it grows to 5478 distinct nodes, consistent with
           http://en.wikipedia.org/wiki/Game_complexity#Example:_tic-tac-toe
        '''
        self.node.grow() # .....
        self.assertTrue(game_tree.distinct_node_count(self.node) == 5478)
        
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestNearlyFull)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestEmpty)
unittest.TextTestRunner(verbosity=2).run(suite1)
unittest.TextTestRunner(verbosity=2).run(suite2)
