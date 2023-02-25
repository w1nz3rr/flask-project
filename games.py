import random
from flask import Flask, render_template
from flask import redirect, request
app = Flask(__name__)


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
        self.win = 0

    def update_win(self, win):
        self.win = win

    def set_win(self):
        li = ['-', 'Ваше число больше', 'Ваше число меньше', 'некорректный ввод', 'победа']
        return li[self.win]

    def check_luck(self):
        if self.x > self.y:
            self.win = 1
            Luck.update_r(self)
        elif self.x < self.y:
            self.win = 2
            Luck.update_l(self)
        elif self.x == self.y:
            self.win = 4
        Luck.update_count(self)


k = Knb()
g = Bm()
luck = Luck()


html = '''<html>
   <body>
      <form action = "http://localhost:5000/resgame1" method = "post">
         <p>Введите ответ:</p>
         <p><input type = "text" name = "answer" placeholder='ответ'/></p>
         <p><input type = "submit" value = "отправить" /></p>
      </form>
   </body>
</html>'''
htmll = '''<html>
   <body>
      <form action = "http://localhost:5000/ress" method = "post">
         <p>Введите ответ:</p>
         <p><input type = "text" name = "answerr" placeholder='ответ'/></p>
         <p><input type = "submit" value = "отправить" /></p>
      </form>
   </body>
</html>'''
htmlll = '''<html>
    <body>
       <form action = "http://localhost:5000/res_luck" method = "post">
          <p>Введите ответ:</p>
          <p><input type = "text" name = "answer_luck" placeholder='ответ'/></p>
          <p><input type = "submit" value = "отправить" /></p>
       </form>
    </body>
 </html>'''
style = '''
    <style>
        html{
            background: url("https://cdn.discordapp.com/attachments/1044693632768282778/1079094981320527972/img.png") no-repeat center center fixed;
        }
        *{
            color: burlywood;
            text-decoration: none;
        }

        a{
            display: inline-block;
            padding: 10px 15px;
            border: 1px solid burlywood;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        a:hover{
            color: orangered;
            border: 1px solid orangered;
        }
        
        input{
            background: inherit;
            border: 1px solid burlywood;
            border-radius: 10px;
            padding: 10px 15px;
        }
    </style>
'''

#фунции 1ой игры
@app.route('/')
def choose():
    return render_template('pravila.html')


@app.route('/rullgame1')
def rullgame1():
    return render_template('rullgame1.html')


@app.route('/game1')
def yes_or_no():
    return f'<div>' \
           f'{style}'\
           f'{g.number()}' \
           f' {html}' \
           f'Счет на данный момент:{g.get_count()}<br>' \
           f'<title>БольшеМеньше</title>' \
           f' <a href="/">выбрать другую игру </a><br>'\
           f'</div>'


@app.route('/resgame1', methods=['POST', 'GET'])
def get_answer():
    if request.method == 'POST':
        answer = request.form['answer']
        x = g.get_x()
        y = g.get_y()
        if (answer == 'да' and y > x) or (answer == 'нет' and y < x):
            g.upload_count()
            g.upload_x()
            g.upload_y()
            return redirect('/game1')
        elif (answer == 'да' and y < x) or (answer == 'нет' and y > x):
            return redirect('/lose')
        else:
            return redirect('/game1')
    else:
        return redirect('/game1')


@app.route('/lose')
def loser():
    new_count = g.get_count()
    lose_x = g.get_x()
    lose_y = g.get_y()
    g.null_count()
    g.random_x()
    g.upload_y()
    return f'<div>' \
           f'{style}' \
           f'Ваше число было {str(lose_x)}, а следующее число было {str(lose_y)}<br>' \
           f'Итоговый счет:{str(new_count)}<br>' \
           f'   <a href="/game1">начать снова</a>' \
           f'</div>'

#фунции 2ой игры
@app.route('/rullgame2')
def rullgame2():
    return render_template('rullgame2.html')


@app.route('/game2')
def gameplay():
    l = ['камень', 'ножницы', 'бумага', '-']
    return f'<div>' \
           f'{style}' \
           f' {htmll}' \
           f'Ваш ответ : {k.get_x()}</br>'\
           f'Ответ компьютера: {l[k.get_y()]}</br>' \
           f'итог = {k.get_win()}</br>' \
           f' <a href="/">выбрать другую игру </a><br>' \
           f'<title>КНБ</title>'\
           f'</div>'


@app.route('/ress', methods=['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        answerr = request.form['answerr']
        k.upload_x(answerr)
        k.upload_y()
        l = ['камень', 'ножницы', 'бумага', '-']
        y = l[k.get_y()]
        if (answerr == 'камень' and y == 'ножницы') or (answerr == 'ножницы' and y == 'бумага') or (answerr == 'бумага' and y == 'камень'):
            k.upload_c(3)
            return redirect('/game2')
        elif (answerr == 'камень' and y == 'бумага') or (answerr == 'ножницы' and y == 'камень') or (answerr == 'бумага' and y == 'ножницы'):
            k.upload_c(2)
            return redirect('/game2')
        elif answerr == y:
            k.upload_c(1)
            return redirect('/game2')
        else:
            k.upload_c(0)
            return redirect('/game2')
    else:
        return redirect('/game2')



#фунции 3ей игры
@app.route('/rullgame3')
def rullgame3():
     return render_template('rullgame3.html')


@app.route('/game3')
def game_luck():
     return f'<div>' \
            f'{style}' \
            f' {htmlll}' \
            f'Предел от {luck.get_l()} до {luck.get_r()}</br>' \
            f'Количество попыток {luck.get_count()} </br>' \
            f'Итого {luck.set_win()} </br>' \
            f' <a href="/">выбрать другую игру </a><br>'\
            f'<title>luck</title>' \
            f'</div>'


@app.route('/res_luck', methods=['POST', 'GET'])
def get_res():
     l, r = luck.get_l(),luck.get_r()
     y = luck.get_y()
     if request.method == 'POST':
         x = request.form['answer_luck']
         if x == 'рестарт':
             luck.null()
             return redirect('/game3')
         x = int(x)
         if (x < l) or (x > r):
             luck.update_win(3)
             return redirect('/game3')
         luck.update_x(x)
         luck.check_luck()
         return redirect('/game3')
     else:
         return redirect('/game3')


@app.route('/win_luck')
def win_luck():
     new_count = luck.get_count()
     luck.null()
     f'{style}' \
     f'<div>' \
     f'Победа<br>' \
     f'Итоговое количество попыток:{str(new_count)}<br>' \
     f'   <a href="/res_luck">начать снова<br>' \
     f'{luck.null()}' \
     f'   <a href="/">выбрать другую игру</a>' \
     f'</div>' \

luck.null()


if __name__ == '__main__':
    app.run(debug=True)

