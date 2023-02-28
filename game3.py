import random


class Luck:

    def __init__(self, x=0, y=random.randrange(2, 100), l=1, r=100, count=0, win=0):
        self.x = x
        self.y = y
        self.l = l
        self.r = r
        self.count = count
        self.win = win

    def update_count(self):
        self.count += 1


    def get_count(self):
        return self.count

    def update_l(self):
        self.l = self.x

    def update_r(self):
        self.r = self.x

    def update_x(self, x):
        self.x = x

    def get_l(self):
        return self.l

    def get_r(self):
        return self.r

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def null(self):
        self.l = 1
        self.r = 100
        self.y = random.randrange(2, 100)
        self.count = 0

    def update_win(self, win):
        self.win = win

    def set_win(self):
        li = ['-', 'Ваше число больше', 'Ваше число меньше', 'некорректный ввод', 'победа']
        return li[self.win]

    def check_luck(self):
        Luck.update_count(self)
        if self.x > self.y:
            self.win = 1
            Luck.update_r(self)
        elif self.x < self.y:
            self.win = 2
            Luck.update_l(self)
        elif self.x == self.y:
            self.win = 4
            Luck.null(self)

