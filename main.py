import random
from flask import Flask, render_template
from flask import redirect, request
app = Flask(__name__)
from game1 import *
from game2 import *
from game3 import *
from style_and_html import *


g = Bm()
k = Knb()
luck = Luck()


@app.route('/')
def choose():
    return render_template('home.html')


@app.route('/rullgame1')
def rullgame1():
    return render_template('rullgame1.html')


@app.route('/game1')
def yes_or_no():
    return f'<div>' \
           f'{style}'\
           f'{g.number()}' \
           f' {html_game1}' \
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

@app.route('/rullgame2')
def rullgame2():
    return render_template('rullgame2.html')


@app.route('/game2')
def gameplay():
    l = ['камень', 'ножницы', 'бумага', '-']
    return f'<div>' \
           f'{style}' \
           f' {html_game2}' \
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



@app.route('/rullgame3')
def rullgame3():
     return render_template('rullgame3.html')


@app.route('/game3')
def game_luck():
     return f'<div>' \
            f'{style}' \
            f' {html_game3}' \
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

