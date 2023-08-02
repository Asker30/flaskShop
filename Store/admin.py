from Store import store, db, models
from flask import request, render_template, redirect, url_for

NAME = "admin"
PASSWORD = 'default'

session = dict()

def create_admin(name=NAME, password=PASSWORD):
    if not(check_admin(name, password)):
        user = models.Users(name=name, psw=password, user_type='admin')
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
            
@store.route('/admin/login')            
def admin_login():
    if request.form:
        name = request.form['name']
        psw = request.form['psw']
        if check_admin(name, psw):
            session['username'] = name
            return redirect(url_for('admin_login'))
        
    return render_template('login.html' )
    

def check_admin(name=None, password=None):
    if name and password:
        user = models.Users.query.filter_by(name=name, psw=password, user_type='admin').first()
        if user:
            return True
    return False