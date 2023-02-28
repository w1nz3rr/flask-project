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