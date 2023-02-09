from flask import Flask, url_for

app = Flask('app')


@app.route('/')
def index():
    return f"""
<!doctype html>
<html>
<head>
</head>
<body>
<h1>Миссия Колонизация Марса</h1>
</body>
</html>
"""


@app.route('/index/')
def index1():
    return f"""
<!doctype html>
<html>
<head>
</head>
<body>
<h1>И на Марсе будут яблони цвести!</h1>
</body>
</html>
"""

@app.route('/promotion/')
def index2():
    return f"""
<!doctype html>
<html>
<head>
</head>
<body>
<b>
Человечество вырастает из детства.</br></br>
Человечеству мала одна планета.</br></br>
Мы сделаем обитаемыми безжизненные пока планеты.</br></br>
И начнем с Марса!</br></br>
Присоединяйся!
</b>
</body>
</html>
"""

@app.route('/image_mars/')
def index3():
    return f"""
<!doctype html>
<html>
<head>
</head>
<body>
<h1>Жди нас марс.</h1></br>
<img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"></br>
Вот она какая, красная планета.
</body>
</html>
"""


app.run(debug='True', port=8080)
