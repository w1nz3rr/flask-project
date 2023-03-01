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



