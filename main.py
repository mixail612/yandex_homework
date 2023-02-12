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


@app.route('/promotion_image/')
def promotion():
    return f"""
<!doctype html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
<link rel="stylesheet" 
href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
crossorigin="anonymous">
</head>
<body>
<h2>Жди нас марс.</h2></br>
<img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"></br>
<div class="alert alert-dark" role="alert">
        <h5>Человечество вырастет из детства.</h5>
</div>
<div class="alert alert-success" role="alert">
        <h5>Человечеству мала одна планета.</h5>
</div>
<div class="alert alert-secondary" role="alert">
        <h5>Мы сделаем обитаемыми безжизненные пока планеты.</h5>
</div>
<div class="alert alert-warning" role="alert">
        <h5>И начнем с марса!</h5>
</div>
<div class="alert alert-danger" role="alert">
        <h5>Присоединяйся!</h5>
</div>
</body>
</html>
"""



app.run(debug='True', port=8080)
