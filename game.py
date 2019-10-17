import unittest

class Game(object):

    def check(self, sq):
        t = [
            sq[0] + sq[1] + sq[2],
            sq[3] + sq[4] + sq[5],
            sq[6] + sq[7] + sq[8],
            sq[0] + sq[3] + sq[6],
            sq[1] + sq[4] + sq[7],
            sq[2] + sq[5] + sq[8],
            sq[0] + sq[4] + sq[8],
            sq[2] + sq[4] + sq[6],
        ]
        for i in range(8):
            if t[i] == 'XXX':
                return True
            if t[i] == 'OOO':
                return True
        return False

    def corr(self, num, sq):
        try:
            tr = int(num)
        except ValueError:
            return False
        if tr < 1:
            return False
        if tr > 9:
            return False
        if sq[tr - 1] == num:
                return True
        return False

    def rstr(self, i, sq):
        return "|%s|%s|%s|" % (sq[0 + i * 3], sq[1 + i * 3], sq[2 + i * 3])

    def start(self):
        a = ['X', 'O']
        sq = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for j in range(3):
            print(play.rstr(j, sq))
        for i in range(9):
            print("Step, %s:" % (i))
            while 1:
                print("Your move, %s:" % (a[i % 2]))
                num = input()
                if play.corr(num, sq) == True:
                    break
                print("Your input is incorrect")
            sq[int(num) - 1] = a[i % 2]
            for j in range(3):
                print(play.rstr(j, sq))
            if play.check(sq) == True:
                print(a[i % 2], " win!")
                return
        print("Draw")
        return

class TestGame(unittest.TestCase):

    def test_rstr(self):
        tplay = Game()
        tsq = ['1', '2', 'X', '4', '5', '6', 'O', 'X', '9']
        self.assertEqual(tplay.rstr(0, tsq), '|1|2|X|')
        self.assertEqual(tplay.rstr(1, tsq), '|4|5|6|')
        self.assertEqual(tplay.rstr(2, tsq), '|O|X|9|')
        
    def test_correct(self):
        tplay = Game()
        tsq = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.assertTrue(tplay.corr('7', tsq))
        self.assertFalse(tplay.corr('1000',  tsq))
    
    def test_check(self):
        tplay = Game()
        self.assertTrue(tplay.check(['X', 'X', 'X', '4', 'O', 'O', '7', '8', '9']))
        self.assertFalse(tplay.check(['X', 'O', 'X', '4', 'O', 'O', '7', 'X', '9']))
        
if __name__ == "__main__":
    play = Game()
    play.start()
    unittest.main()