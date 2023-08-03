from Store import store, db, models
from flask import request, render_template, redirect, url_for

BASE_URL = '/admin'
NAME = "admin"
PASSWORD = 'default'

session = list()

@store.route('/admin/')
def admin_root():
    "Переадресация"
    if session:
        return redirect(url_for('database_list'))
    return redirect(url_for('admin_login'))

@store.route(BASE_URL + '/table/', methods=['GET'])
def database_list():
    """Список таблиц из БД"""
    if session:
        return render_template('database_list.html')
    return redirect(url_for('admin_login'))

@store.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Добавление данных в таблицу с продуктами"""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        photo = request.files['photo']
        price = float(request.form['price'])
        count = int(request.form['count'])

        # Сохраняем загруженное изображение в папку 'static/photos'
        photo.save(f'D:/PetPoject/flaskShop/Store/img/{photo.filename}')

        # Создаем экземпляр объекта Product и добавляем его в базу данных
        new_product = models.Product(title=title, description=description, img=photo.filename, price=price, count=count)
        try:
            db.session.add(new_product)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

        return 'Продукт успешно добавлен в базу данных!'

    return render_template('add_product.html')

@store.route(BASE_URL + '/login', methods=['POST', 'GET'])            
def admin_login():
    """Страница входа в админку"""
    if request.form:
        name = request.form['name']
        psw = request.form['psw']
        if check_admin(name, psw):
            session.append(name) 
            return redirect(url_for('database_list'))
        
    return render_template('login.html' )

@store.route(BASE_URL + '/logout')
def admin_logout():
    """Выход из админ аккаунта"""
    session.pop()
    return redirect(url_for('admin_login'))

def check_admin(name=None, password=None):
    """Проверка имеет ли аккаунт права админа"""
    if name and password:
        user = models.Users.query.filter_by(name=name, psw=password, user_type='admin').first()
        if user:
            return True
    return False

def create_admin(name=NAME, password=PASSWORD):
    """Создание админ аккаунта"""
    if not(check_admin(name, password)):
        user = models.Users(name=name, psw=password, user_type='admin')
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()