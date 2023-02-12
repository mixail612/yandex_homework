from flask import Flask, url_for, request

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


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" id="fam" name="fam" placeholder="Введите фамилию"></br>
                                    <input type="text" id="name" name="name" placeholder="Введите имя"></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                     <fieldset>
                                          <legend>Какие у вас есть профессии?</legend>
                                          <div>
                                            <input type="checkbox" id="ing-i" name="profession" value="ing-i" />
                                            <label for="ing-i">Инженер-исследователь</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="ing-s" name="profession" value="ing-s" />
                                            <label for="ing-s">Инженер-строитель</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="pilot" name="profession" value="pilot" />
                                            <label for="pilot">Пилот</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="met" name="profession" value="met" />
                                            <label for="met">Метеоролог</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="ing-j" name="profession" value="ing-j" />
                                            <label for="ing-j">Инженер по жизнеобеспечению</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="ing-r" name="profession" value="ing-r" />
                                            <label for="ing-r">Инженер по радиационной защите</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="doctor" name="profession" value="doctor" />
                                            <label for="doctor">Врач</label>
                                          </div>
                                          <div>
                                            <input type="checkbox" id="ekz" name="profession" value="ekz" />
                                            <label for="ekz">Экзобиолог</label>
                                          </div>
                                    </fieldset>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['fam'])
        print(request.form['name'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        return "Форма отправлена"



app.run(debug='True', port=8080)
