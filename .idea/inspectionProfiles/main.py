from flask import Flask
app = Flask(__name__)

html = '''<html>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>   
   </body>
</html>'''


class Shop:
    def __init__(self):
        self.data = []

    def push_new_buy(self, item, quantity, package):
        record = (item, quantity, package)
        self.data.append(record)

    def __str__(self):
        s = ''
        max_size = 10
        for el in self.data:
            ell = el[0] + ' ' * (max_size - len(el[0]))
            s += f'{ell} | {el[1]} | {el[2]}<br>'
        return s

shop = Shop()
shop.push_new_buy('Молоко', 3, 'л')
shop.push_new_buy('Гречка', 3, 'кг')


@app.route('/')
def hello_world():
    return str(shop)

if __name__ == '__main__':
    app.run()