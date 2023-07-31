from Store import store, models, db
from flask import redirect, url_for, request, render_template, abort

BASE_URL = r'/Shop.store'
session = dict() # Словарь для хранения данных о пользователе

@store.route('/')
def root_redirect():
    return redirect(url_for('base'))

@store.route(BASE_URL + '/', methods=['GET'])
def base():
    """Базовая страница"""
    if session:
        return render_template('base.html', name=session['username'])
    else:
        return redirect(url_for('register'))

@store.route(BASE_URL + '/register', methods=['POST', 'GET'])
def register():
    """Регистрация"""
    if request.form:
        name = request.form['name']
        email = request.form['email']
        psw = request.form['password']
        user = models.Users(name=name, email=email, psw=psw)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            abort(404)
        finally:
            db.session.close()

    return render_template('register.html')

@store.route(BASE_URL + '/login', methods=['POST', 'GET'])
def login():
    """Вход в аккаунт"""
    if request.form:
        name = request.form['name']
        psw = request.form['psw']
        if check_login(name, psw):
            session['username'] = name
            return redirect(url_for('base'))
        
    return render_template('login.html' )

@store.route(BASE_URL + '/logout')
def logout():
    """Выход из аккаунта"""
    session = dict()
    return redirect(url_for('login'))
    
    
def check_login(name=None, password=None) -> bool:
    """Проверка существует ли такой пользователь"""
    if name and password:
        user = models.Users.query.filter_by(name=name, psw=password).first()
        if user:
            return True
    return False