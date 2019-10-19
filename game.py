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
            while True:
                num = input("Your move, %s:" % (a[i % 2]))
                if play.corr(num, sq):
                    break
                print("Your input is incorrect")
            sq[int(num) - 1] = a[i % 2]
            for j in range(3):
                print(play.rstr(j, sq))
            if play.check(sq):
                print(a[i % 2], " win!")
                return
        print("Draw")
        return
        
if __name__ == "__main__":
    play = Game()
    play.start()