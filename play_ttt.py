from tic_tac_toe import *
#play tic tac toe



if __name__ == '__main__':
    
    r = 'yes'
    
    while r.lower() == 'yes':
    
        #Create a new game
        t = TicTacToe(([[None,None,None],[None,None,None],[None,None,None]],'p2'))
        #t = TicTacToe(([['p1','p2','p1'],[None,'p2',None],[None,None,None]],'p1'))        
    
        while not t.winner('p2') and not t.winner('p1') and not len(t.next_move()) == 0:
            print t
            if t.player() == 'p1':
                p_move = raw_input('Enter move: ')
            
                the_move = (int(p_move.split(',')[0]), int(p_move.split(',')[1]))
                t = t.make_move(the_move)
            else:
                m = t.minimax(999999)[0]
                t = t.make_move(m)
        
        
        if t.winner('p1'):
            print t
            print 'p1 is the winner!'
        
        if t.winner('p2'):
            print t
            print 'p2 is the winner!'
            
            
        r = raw_input('Coninue? yes/no: ')