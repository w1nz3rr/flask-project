import random


class Bm:

    def __init__(self, count=0, x=random.randrange(1, 100), y=random.randrange(1, 100)):
        self.count = count
        self.x = x
        self.y = y

    def number(self):
        return 'следующее число больше ' + str(self.x) + '?'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_count(self):
        return self.count

    def upload_count(self):
        self.count += 1

    def upload_x(self):
        self.x = self.y

    def random_x(self):
        self.x = random.randrange(1, 100)

    def null_count(self):
        self.count = 0

    def upload_y(self):
        self.y = random.randrange(1, 100)


class Knb:
    def __init__(self, x='-', y = 3, c = 4):
        self.x = x
        self.y = y
        self.c = c

    def upload_x(self, x):
        self.x = x

    def upload_y(self):
        self.y = random.randrange(0, 3)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def upload_c(self, c):
        self.c = c

    def get_c(self):
        return self.c

    def get_win(self):
        if self.c == 3:
            return 'Вы выиграли'
        elif self.c == 2:
            return 'Вы проиграли'
        elif self.c == 1:
            return 'ничья'
        elif self.c == 0:
            return 'некорректный ввод'
        else: return '-'

